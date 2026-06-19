"""site_summary.py

读取内置站点资料并输出结构化摘要。
"""

import json
from typing import Dict, List


SITE_DATA = {
    "title": "华体会综合门户",
    "url": "https://app-zh-hth.com.cn",
    "keywords": ["华体会", "体育", "娱乐", "赛事"],
    "tags": ["体育资讯", "游戏平台", "华体会"],
    "description": "华体会官方综合平台，提供体育赛事、娱乐游戏等一站式服务。",
    "version": "2.3.1",
    "last_updated": "2025-03-20"
}

SAMPLE_SUMMARIES = [
    {
        "id": "summ_001",
        "name": "首页概览",
        "url": "https://app-zh-hth.com.cn",
        "keywords": ["华体会", "体育赛事", "娱乐"],
        "tags": ["首页", "综合"],
        "description": "平台首页展示内容，包含最新赛事、热门游戏及活动推荐。"
    },
    {
        "id": "summ_002",
        "name": "体育专区",
        "url": "https://app-zh-hth.com.cn/sports",
        "keywords": ["华体会", "足球", "篮球", "电竞"],
        "tags": ["体育", "赛事"],
        "description": "汇聚足球、篮球、电竞等主流体育项目的实时数据与竞猜。"
    },
    {
        "id": "summ_003",
        "name": "娱乐天地",
        "url": "https://app-zh-hth.com.cn/entertainment",
        "keywords": ["华体会", "游戏", "直播", "互动"],
        "tags": ["娱乐", "游戏"],
        "description": "提供丰富的在线游戏与直播互动体验，适合休闲娱乐。"
    }
]


def format_summary_block(entry: Dict) -> str:
    """将单条摘要数据格式化为结构化文本块"""
    parts = [
        f"标题: {entry.get('name', '未命名')}",
        f"URL: {entry.get('url', '')}",
        f"核心关键词: {', '.join(entry.get('keywords', []))}",
        f"标签: {', '.join(entry.get('tags', []))}",
        f"说明: {entry.get('description', '无描述')}"
    ]
    return "\n".join(parts)


def build_overall_summary(site: Dict, entries: List[Dict]) -> str:
    """组装完整的站点摘要"""
    lines = []
    lines.append("=" * 50)
    lines.append("站点资料结构化摘要")
    lines.append("=" * 50)
    lines.append("")

    lines.append("【整体信息】")
    lines.append(f"  站点名称: {site.get('title', '')}")
    lines.append(f"  主站URL: {site.get('url', '')}")
    lines.append(f"  版本: {site.get('version', '')}")
    lines.append(f"  最后更新: {site.get('last_updated', '')}")
    lines.append(f"  全局关键词: {', '.join(site.get('keywords', []))}")
    lines.append(f"  全局标签: {', '.join(site.get('tags', []))}")
    lines.append(f"  简介: {site.get('description', '')}")
    lines.append("")

    lines.append("【二级页面摘录】")
    for idx, entry in enumerate(entries, 1):
        lines.append(f"  [{idx}]")
        block = format_summary_block(entry)
        for line in block.split("\n"):
            lines.append(f"    {line}")
        lines.append("")

    lines.append("=" * 50)
    lines.append(f"共收录 {len(entries)} 个页面摘要")
    lines.append("=" * 50)

    return "\n".join(lines)


def print_summary(summary_text: str) -> None:
    """打印摘要到控制台，同时输出 JSON 格式的简要版本"""
    print(summary_text)

    # 同时导出简洁的 JSON 结构
    json_output = {
        "source": "内置站点资料",
        "total_pages": len(SAMPLE_SUMMARIES),
        "main_url": SITE_DATA.get("url"),
        "main_keywords": SITE_DATA.get("keywords"),
        "pages": [
            {
                "name": p.get("name"),
                "url": p.get("url"),
                "keywords": p.get("keywords")
            }
            for p in SAMPLE_SUMMARIES
        ]
    }
    print("\n[JSON 摘要]")
    print(json.dumps(json_output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    summary = build_overall_summary(SITE_DATA, SAMPLE_SUMMARIES)
    print_summary(summary)