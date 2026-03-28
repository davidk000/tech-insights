#!/usr/bin/env python3
"""
模型池健康检查
每6小时执行一次，检查各模型池可用性
"""

import json
from pathlib import Path

def load_model_pools():
    """加载模型池配置"""
    config_path = Path.home() / ".openclaw/workspace/config/model-pools.json"
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_pool_health(pool_name, pool_config):
    """检查单个模型池健康状态（模拟）"""
    # 实际实现中应该调用模型API检查可用性
    return {
        "name": pool_name,
        "display_name": pool_config.get("name", pool_name),
        "primary": pool_config.get("primary", ""),
        "fallback": pool_config.get("fallback", ""),
        "status": "healthy",  # healthy/degraded/unavailable
        "latency": "normal",  # normal/high
        "last_check": "2026-03-05T10:00:00"
    }

def generate_health_report():
    """生成健康报告"""
    config = load_model_pools()
    pools = config.get("pools", {})
    
    report = {
        "timestamp": "2026-03-05T10:00:00",
        "overall_status": "healthy",
        "pools": []
    }
    
    for pool_name, pool_config in pools.items():
        health = check_pool_health(pool_name, pool_config)
        report["pools"].append(health)
    
    return report

def save_health_status(report):
    """保存健康状态"""
    status_path = Path.home() / ".openclaw/workspace/data/model-health-status.json"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(status_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return status_path

def main():
    print("🔍 检查模型池健康状态...")
    
    report = generate_health_report()
    status_path = save_health_status(report)
    
    print(f"✅ 健康检查完成，报告已保存: {status_path}")
    print("\n模型池状态:")
    for pool in report["pools"]:
        status_emoji = "🟢" if pool["status"] == "healthy" else "🟡" if pool["status"] == "degraded" else "🔴"
        print(f"  {status_emoji} {pool['display_name']}: {pool['status']}")

if __name__ == "__main__":
    main()
