import requests
import re
import math

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def bilibili163637592():
    url = 'https://api.bilibili.com/x/space/arc/search?mid=163637592&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    #https://space.bilibili.com/163637592/video?tid=0&page=2&keyword=&order=pubdate  第二页
    response = requests.get(url,headers=headers)
    info = response.text
    name = re.findall('"name":"(.*?)"}',info)
    count = re.findall(',"count":(.*?),"',info)
    print(info)
    print(name)
    print(count)

def bilibiligetpage(id):
    url = 'https://api.bilibili.com/x/space/arc/search?mid='+id+'&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    response = requests.get(url,headers=headers)
    info = response.text
    count = re.findall('"page":{"count":(.*?),',info)
    x = math.ceil(int(count[0]) / 30)  #向上取整
    print(x)
    return(x)

print(bilibiligetpage('163637592'))

