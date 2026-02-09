#!/usr/bin/env python3
"""简单的图片上传包装器"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from publisher import WeChatPublisher

def upload_single_image(image_path: str, return_url: bool = True):
    if not os.path.exists(image_path):
        print(f"错误: 图片文件不存在: {image_path}", file=sys.stderr)
        sys.exit(1)

    publisher = WeChatPublisher()
    result = publisher.upload_image(image_path, return_url=return_url)

    if return_url:
        media_id, url = result
        print(f"media_id: {media_id}")
        print(f"url: {url}")
    else:
        print(f"media_id: {result}")

    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python image_uploader.py <图片路径> [--no-url]")
        sys.exit(1)

    image_path = sys.argv[1]
    return_url = '--no-url' not in sys.argv
    upload_single_image(image_path, return_url)
