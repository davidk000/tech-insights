#!/bin/bash
# 每日早报归档脚本
# 归档到 tech-insights/daily-news/YYYY/MM/YYYY-MM-DD.md
# 用法: ./daily-news-archive.sh "2026-03-24" "早报内容..."

# 修复: tech-insights/ 在 .gitignore 中，改用 daily-news.local/ (tracked)
ARCHIVE_DIR="$HOME/.openclaw/workspace/daily-news.local"
DATE="${1:-$(date +%Y-%m-%d)}"
CONTENT="${2:-}"

YEAR=$(echo "$DATE" | cut -d'-' -f1)
MONTH=$(echo "$DATE" | cut -d'-' -f2)
TARGET_DIR="$ARCHIVE_DIR/$YEAR/$MONTH"

mkdir -p "$TARGET_DIR"

FILENAME="$TARGET_DIR/${DATE}.md"

cat > "$FILENAME" << EOF
---
date: $DATE
created_at: $(date '+%Y-%m-%d %H:%M:%S')
type: daily-news
---

# 科技早报 - $DATE

$CONTENT

---
*归档时间: $(date '+%Y-%m-%d %H:%M:%S')*
EOF

echo "已归档到: $FILENAME"
