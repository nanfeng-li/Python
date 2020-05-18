import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url = 'https://space.bilibili.com/375375'
response = requests.get(url,headers=headers)
# a = eval("u" + "\'" + response.text + "\'")
# print(a)
a = response.text

print(a)
# name = re.findall('<strong>(.*?)</strong>',a)
# name1= []
# for i in name:
#     if i not in name1:
#         name1.append(i)
# print(name1)
# print(name)
#