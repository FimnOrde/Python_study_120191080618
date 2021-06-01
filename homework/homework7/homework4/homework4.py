'''
homework4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
'''
import requests
from lxml import etree

result_txt = open('result.txt', 'w', encoding='utf-8')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}
response = requests.get('https://www.programcreek.com/python/example/3765/requests.get', headers=headers)
html_tree = etree.HTML(response.text)
pre_list = html_tree.xpath('//pre[@class="prettyprint"]')
n = 0

for pre in pre_list:
    n += 1
    code = ''.join([i.strip() for i in pre.xpath('.//text()')])
    string = f'Example {n}' + '\n\n'
    string += code + '\n' + '*' * 100
    print(string)
    result_txt.write(string + '\n')
result_txt.close()
