#!/usr/bin/env python3
"""
Heartbeat检查脚本
每30分钟执行一次，维护记忆和学习
注意：只更新 heartbeat-state.json，不触碰 HEARTBEAT.md（任务定义在里面）
"""

import os
import json
import datetime
from pathlib import Path

def get_state_path():
    return Path.home() / ".openclaw/workspace/data/heartbeat-state.json"

def load_state():
    state_path = get_state_path()
    if state_path.exists():
        with open(state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "last_run": None,
        "daily_tasks_completed": False,
        "weekly_tasks_completed": False,
        "run_count": 0
    }

def save_state(state):
    state_path = get_state_path()
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def check_daily_tasks():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    tasks = []

    if hour == 22 and minute < 30:
        tasks.append("生成每日进化报告")
    if hour == 9 and minute < 30:
        tasks.append("生成每日成长报告")
    if minute < 5:
        tasks.append("深度学习1个skill")

    return tasks

def check_memory_maintenance():
    now = datetime.datetime.now()
    return [
        "检查紧急事项",
        "整理今日记忆",
        "清理7天前日志"
    ]

def main():
    print("Heartbeat检查中...")

    state = load_state()
    state["last_run"] = datetime.datetime.now().isoformat()
    state["run_count"] = state.get("run_count", 0) + 1

    memory_tasks = check_memory_maintenance()
    daily_tasks = check_daily_tasks()

    print(f"记忆维护: {memory_tasks}")
    print(f"定时任务: {daily_tasks}")
    print(f"运行次数: {state['run_count']}")

    save_state(state)
    print("Heartbeat检查完成")

if __name__ == "__main__":
    main()
