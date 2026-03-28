#!/usr/bin/env python3
"""
每日进化报告生成器
每日22:00执行，生成AI自我进化报告
"""

import os
import json
import datetime
from pathlib import Path

def load_knowledge_base():
    """加载技能知识库"""
    kb_path = Path.home() / ".openclaw/workspace/data/skill-knowledge-base.json"
    if kb_path.exists():
        with open(kb_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"skills": [], "integrations": []}

def get_today_memory_files():
    """获取今天的记忆文件"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    memory_dir = Path.home() / ".openclaw/workspace/memory"
    files = list(memory_dir.glob(f"{today}*.md"))
    return files

def generate_evolution_report():
    """生成进化报告"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    kb = load_knowledge_base()
    memory_files = get_today_memory_files()
    
    report = f"""# 🧬 每日进化报告 - {today}

## 📊 今日统计

- 📝 记忆文件数：{len(memory_files)}
- 🧩 技能总数：{len(kb.get('skills', []))}
- 🔗 技能组合：{len(kb.get('integrations', []))}
- 📅 知识库更新：{kb.get('last_updated', '未记录')}

## 🧠 已掌握技能

"""
    
    for skill in kb.get('skills', [])[-5:]:  # 最近5个
        report += f"- **{skill['name']}** ({skill['category']})\n"
        report += f"  - 知识点：{len(skill.get('knowledge_points', []))}个\n"
        report += f"  - 最佳实践：{len(skill.get('best_practices', []))}条\n"
    
    report += """
## 🔧 建议固化的技能

基于使用频率和通用性，建议固化以下技能：

1. **待识别** - 记录重复出现的任务模式
2. **待识别** - 总结高效的工作流程
3. **待识别** - 提取可复用的解决方案

## 📅 明日计划

- [ ] 继续学习新skill
- [ ] 测试技能组合
- [ ] 优化记忆管理

## 💡 成长建议

> "不只是安装skill，而是深度学习其中的知识"

1. 每天深度学习1个已安装的skill
2. 寻找技能之间的关联
3. 尝试组合技能创造新能力
4. 记录经验到知识库

---
*生成时间：{now}*
*学习虾 🦐 - 持续进化中*
""".format(now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    return report

def save_report(report):
    """保存报告"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report_dir = Path.home() / ".openclaw/workspace/data/evolution-reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    report_path = report_dir / f"{today}-evolution-report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    return report_path

def main():
    print("🧬 生成每日进化报告...")
    
    report = generate_evolution_report()
    report_path = save_report(report)
    
    print(f"✅ 报告已保存: {report_path}")
    print("\n" + "="*50)
    print(report)
    print("="*50)
    
    # 同时输出到HEARTBEAT.md格式的任务
    print("\n📋 建议添加到HEARTBEAT.md的任务：")
    print("- [ ] 深度学习1个skill")
    print("- [ ] 检查今日记忆文件，提取重要决策到MEMORY.md")
    print("- [ ] 测试1个技能组合")

if __name__ == "__main__":
    main()
