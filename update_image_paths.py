#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新pokemon_database.js中的图片路径为本地路径
"""

import re

def update_image_paths():
    """将远程图片URL替换为本地路径"""

    # 读取数据库文件
    with open('pokemon_database.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换所有的远程URL为本地路径
    # 从: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/123.png
    # 到: images/pokemon/123.png
    pattern = r'https://raw\.githubusercontent\.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/(\d+)\.png'
    replacement = r'images/pokemon/\1.png'

    updated_content = re.sub(pattern, replacement, content)

    # 统计替换次数
    count = len(re.findall(pattern, content))

    # 写回文件
    with open('pokemon_database.js', 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"✅ 更新完成！")
    print(f"✅ 共更新了 {count} 个图片路径")
    print(f"✅ 远程URL → 本地路径: images/pokemon/*.png")

    # 验证
    if count == 1025:
        print(f"\n🎉 完美！所有1025只宝可梦的图片路径都已更新！")
    else:
        print(f"\n⚠️  警告：预期更新1025个路径，实际更新了{count}个")

if __name__ == "__main__":
    update_image_paths()
