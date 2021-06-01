'''
homework3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
'''
import os

import requests
from lxml import etree

if not os.path.exists('download'):
    os.makedirs('download')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}

response = requests.get('http://www.listeningexpress.com/studioclassroom/ad/', headers=headers)

html_tree = etree.HTML(response.text)

href_list = html_tree.xpath('//*[@id="proglist"]/ul/li/a/@href')

for href in href_list:
    href = href.replace("javascript:p('", '').replace("');", '')
    print(href)
    download_url = f'http://www.listeningexpress.com/studioclassroom/ad/{href}'
    r = requests.get(download_url, headers=headers)
    with open(f'download/{href}', 'wb') as f:
        f.write(r.content)
