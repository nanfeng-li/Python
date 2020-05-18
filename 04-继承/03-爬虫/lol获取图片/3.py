import os
import requests
from urllib import error
import socket

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['name'], herolist.json()['hero']))  # 提取英雄的绰号
hero_title = list(map(lambda x: x['title'], herolist.json()['hero']))  # 提取英雄的名字
hero_number = list(map(lambda x: x['heroId'], herolist.json()['hero']))  # 提取英雄的编号

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir("C:\\Users\\lgz001\\Desktop\\lol\\" + hero_name[i] + "-" + hero_title[i])
        # 进入创建好的文件夹
        os.chdir("C:\\Users\\lgz001\\Desktop\\lol\\" + hero_name[i] + "-" + hero_title[i])
        i += 1
        for k in range(20):
            # 拼接url，如果K小于10中间加两个“0”，否则一个“0”
            if k < 10:
                onehero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + str(j) + '00' + str(k) + '.jpg'
            else:
                onehero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + str(j) + '0' + str(k) + '.jpg'
            try:
                im = requests.get(onehero_link, headers=headers)
            except error.URLError as e:
                if isinstance(e.reason, socket.timeout):
                    print('超时，执行下一个请求')
             #请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()
