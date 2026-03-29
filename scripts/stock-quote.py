#!/usr/bin/env python3
"""
stock-quote.py - 金融虾 A 股行情查询工具
使用 easyquotation（腾讯行情源）获取实时行情

用法:
  python3.8 scripts/stock-quote.py --index      # 主要指数
  python3.8 scripts/stock-quote.py 600519      # 个股（自动识别沪/深）
  python3.8 scripts/stock-quote.py 000651 300750  # 多只股票
  python3.8 scripts/stock-quote.py --watch      # 实时监控（Ctrl+C退出）
"""

import sys
import easyquotation as eq

# 腾讯源主要指数代码（内部用带前缀格式，查询时转纯数字）
INDEX_CODES = {
    'sh000001': '上证指数',
    'sz399001': '深证成指',
    'sz399006': '创业板指',
    'sz399005': '中小100',
    'sh000300': '沪深300',
    'sh000016': '上证50',
    'sh000688': '科创50',
}

def format_stock(code, info):
    name = info.get('name', '未知')
    now = info.get('now', 0)
    pct = info.get('涨跌(%)', 0)
    high = info.get('high', 0)
    low = info.get('low', 0)
    pe = info.get('PE', 'N/A')

    direction = '▲' if pct > 0 else ('▼' if pct < 0 else '—')
    emoji = '🔴' if pct > 0 else ('🟢' if pct < 0 else '⚪')

    return (f"{emoji} {name}({code}) "
            f"现价:{now:.2f} {direction}{abs(pct):.2f}% "
            f"高:{high:.2f} 低:{low:.2f} PE:{pe}")

def to_query_code(raw):
    """将股票代码转为腾讯源查询格式（带 sh/sz 前缀）"""
    raw = raw.strip()
    if raw.startswith(('sh', 'sz', 'SH', 'SZ')):
        return raw.lower()
    if raw.isdigit() and len(raw) == 6:
        if raw.startswith('6'):
            return 'sh' + raw
        elif raw.startswith(('0', '3')):
            return 'sz' + raw
    return raw

def strip_prefix(code):
    """去掉 sh/sz 前缀，只保留纯数字代码"""
    return code.lower().lstrip('sh').lstrip('sz')

def main():
    qt = eq.use('tencent')

    if len(sys.argv) < 2 or sys.argv[1] == '--index':
        query_codes = list(INDEX_CODES.keys())
        label = '主要指数'
    elif sys.argv[1] == '--watch':
        query_codes = list(INDEX_CODES.keys())
        label = '实时监控 (Ctrl+C 退出)'
        print(f"\n=== {label} ===")
        try:
            while True:
                data = qt.real(query_codes)
                ts = __import__('datetime').datetime.now().strftime('%H:%M:%S')
                print(f"\n--- {ts} ---")
                for code in query_codes:
                    key = strip_prefix(code)
                    if key in data:
                        print(format_stock(code, data[key]))
                import time; time.sleep(5)
        except KeyboardInterrupt:
            print("\n监控结束")
        return
    else:
        raw_codes = sys.argv[1:]
        query_codes = [to_query_code(c) for c in raw_codes]
        label = f'自选股({len(query_codes)}只)'

    data = qt.real(query_codes)
    print(f"\n=== {label} ===")
    found = 0
    for code in query_codes:
        key = strip_prefix(code)
        if key in data:
            print(format_stock(code, data[key]))
            found += 1
        else:
            print(f"⚠️ {code} 未找到或已下市")
    print(f"\n共获取 {found}/{len(query_codes)} 条")

if __name__ == '__main__':
    main()
