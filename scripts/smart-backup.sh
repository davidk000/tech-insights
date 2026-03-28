#!/bin/bash
# 智能备份脚本
# 触发条件：24小时 或 10K文件变化
# 备份策略：7天轮换（周一~周日）

WORKSPACE="$HOME/.openclaw/workspace"
BACKUP_DIR="$WORKSPACE/.backups"
DAY_OF_WEEK=$(date +%u)  # 1=周一, 7=周日
DATE_STR=$(date +%Y%m%d)

# 核心文件列表
CORE_FILES=(
    "IDENTITY.md"
    "USER.md"
    "SOUL.md"
    "MEMORY.md"
    "HEARTBEAT.md"
    "AGENTS.md"
    "TOOLS.md"
    "config/model-pools.json"
    "data/skill-knowledge-base.json"
)

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 检查是否需要备份
LAST_BACKUP_FILE="$BACKUP_DIR/.last_backup"
NEED_BACKUP=false

if [ ! -f "$LAST_BACKUP_FILE" ]; then
    NEED_BACKUP=true
else
    LAST_BACKUP=$(cat "$LAST_BACKUP_FILE")
    CURRENT_TIME=$(date +%s)
    LAST_TIME=$(stat -c %Y "$LAST_BACKUP_FILE" 2>/dev/null || echo "0")
    TIME_DIFF=$((CURRENT_TIME - LAST_TIME))
    
    # 24小时 = 86400秒
    if [ $TIME_DIFF -gt 86400 ]; then
        NEED_BACKUP=true
    fi
fi

# 检查文件变化
if [ "$NEED_BACKUP" = false ]; then
    TOTAL_SIZE=0
    for file in "${CORE_FILES[@]}"; do
        if [ -f "$WORKSPACE/$file" ]; then
            SIZE=$(stat -c %s "$WORKSPACE/$file" 2>/dev/null || echo "0")
            TOTAL_SIZE=$((TOTAL_SIZE + SIZE))
        fi
    done
    
    LAST_SIZE_FILE="$BACKUP_DIR/.last_size"
    if [ -f "$LAST_SIZE_FILE" ]; then
        LAST_SIZE=$(cat "$LAST_SIZE_FILE")
        SIZE_DIFF=$((TOTAL_SIZE - LAST_SIZE))
        SIZE_DIFF_ABS=${SIZE_DIFF#-}
        
        # 10K = 10240 bytes
        if [ $SIZE_DIFF_ABS -gt 10240 ]; then
            NEED_BACKUP=true
        fi
    else
        NEED_BACKUP=true
    fi
fi

if [ "$NEED_BACKUP" = true ]; then
    echo "🔄 开始备份..."
    
    # 创建当日备份目录
    BACKUP_PATH="$BACKUP_DIR/day-$DAY_OF_WEEK-$DATE_STR"
    mkdir -p "$BACKUP_PATH"
    
    # 备份核心文件
    for file in "${CORE_FILES[@]}"; do
        if [ -f "$WORKSPACE/$file" ]; then
            cp --parents "$WORKSPACE/$file" "$BACKUP_PATH/"
            echo "  ✓ $file"
        fi
    done
    
    # 备份memory目录
    if [ -d "$WORKSPACE/memory" ]; then
        cp -r "$WORKSPACE/memory" "$BACKUP_PATH/"
        echo "  ✓ memory/"
    fi
    
    # 备份config目录
    if [ -d "$WORKSPACE/config" ]; then
        cp -r "$WORKSPACE/config" "$BACKUP_PATH/"
        echo "  ✓ config/"
    fi
    
    # 更新备份记录
    echo "$DATE_STR" > "$LAST_BACKUP_FILE"
    
    # 记录总大小
    TOTAL_SIZE=0
    for file in "${CORE_FILES[@]}"; do
        if [ -f "$WORKSPACE/$file" ]; then
            SIZE=$(stat -c %s "$WORKSPACE/$file" 2>/dev/null || echo "0")
            TOTAL_SIZE=$((TOTAL_SIZE + SIZE))
        fi
    done
    echo "$TOTAL_SIZE" > "$BACKUP_DIR/.last_size"
    
    echo "✅ 备份完成: $BACKUP_PATH"
    echo "📦 备份策略: 7天轮换"
else
    echo "⏭️ 无需备份 (24小时内且变化<10K)"
fi
