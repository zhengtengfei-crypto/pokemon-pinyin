#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载所有宝可梦图片到本地
"""

import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置
IMAGE_DIR = "images/pokemon"
TOTAL_POKEMON = 1025
MAX_WORKERS = 10  # 并发下载数
TIMEOUT = 30  # 请求超时时间（秒）

def create_image_directory():
    """创建图片目录"""
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
        print(f"✅ 创建目录：{IMAGE_DIR}")

def download_image(pokemon_id):
    """下载单个宝可梦图片"""
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    file_path = os.path.join(IMAGE_DIR, f"{pokemon_id}.png")

    # 如果文件已存在，跳过
    if os.path.exists(file_path):
        return (pokemon_id, "exists", None)

    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return (pokemon_id, "success", len(response.content))
        else:
            return (pokemon_id, "failed", f"HTTP {response.status_code}")
    except Exception as e:
        return (pokemon_id, "error", str(e))

def main():
    print("🎮 宝可梦图片下载器")
    print("=" * 60)
    print(f"目标：下载 {TOTAL_POKEMON} 只宝可梦的官方图片")
    print(f"保存位置：{IMAGE_DIR}")
    print(f"并发数：{MAX_WORKERS}")
    print("=" * 60 + "\n")

    # 创建目录
    create_image_directory()

    # 统计
    success_count = 0
    exists_count = 0
    failed_count = 0
    total_size = 0

    start_time = time.time()

    # 使用线程池并发下载
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有下载任务
        futures = {executor.submit(download_image, i): i for i in range(1, TOTAL_POKEMON + 1)}

        # 处理完成的任务
        for future in as_completed(futures):
            pokemon_id, status, info = future.result()

            if status == "success":
                success_count += 1
                total_size += info
                print(f"✅ #{pokemon_id:04d} 下载成功 ({info/1024:.1f} KB)")
            elif status == "exists":
                exists_count += 1
                if exists_count <= 10:  # 只显示前10个已存在的
                    print(f"⏭️  #{pokemon_id:04d} 已存在，跳过")
            else:
                failed_count += 1
                print(f"❌ #{pokemon_id:04d} 下载失败: {info}")

            # 每50个显示一次进度
            total_processed = success_count + exists_count + failed_count
            if total_processed % 50 == 0:
                progress = (total_processed / TOTAL_POKEMON) * 100
                print(f"\n📊 进度：{total_processed}/{TOTAL_POKEMON} ({progress:.1f}%)\n")

    # 完成统计
    elapsed_time = time.time() - start_time

    print("\n" + "=" * 60)
    print("✅ 下载完成！")
    print(f"成功下载：{success_count} 张")
    print(f"已存在：{exists_count} 张")
    print(f"失败：{failed_count} 张")
    print(f"总大小：{total_size / (1024 * 1024):.2f} MB")
    print(f"耗时：{elapsed_time:.1f} 秒")
    print("=" * 60)

    if failed_count > 0:
        print(f"\n⚠️  有 {failed_count} 张图片下载失败，建议重新运行脚本")
    else:
        print("\n🎉 所有图片下载成功！")

if __name__ == "__main__":
    main()
