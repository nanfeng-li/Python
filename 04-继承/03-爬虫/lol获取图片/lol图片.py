import os
import requests

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_Id = list(map(lambda x: x['heroId'], herolist.json()['hero']))  # 提取英雄的id
hero_name = list(map(lambda x: x['name'], herolist.json()['hero']))  # 提取英雄的名称
hero_title = list(map(lambda x: x['title'], herolist.json()['hero']))  # 提取英雄的称号

# 下载图片
def downloadPic():
    i = 0
    for j in hero_Id:
        # 创建文件夹
        os.mkdir("C:\\Users\\lgz001\\Desktop\\lol\\" + hero_title[i]+'-'+hero_name[i])
        # 进入创建好的文件夹
        os.chdir("C:\\Users\\lgz001\\Desktop\\lol\\" + hero_title[i]+'-'+hero_name[i])
        i += 1
        for k in range(20):
            # 拼接url
            if k < 10:
                onehero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'+str(j)+'00'+str(k)+'.jpg'
            else:
                onehero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'+str(j)+'0'+str(k)+'.jpg'

            im = requests.get(onehero_link)
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()
