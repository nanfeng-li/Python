import requests
import re
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def bilibilisj():
    url = 'https://www.biliob.com/api/author?page=0&text=&sort=0'
    response = requests.get(url,headers=headers)
    info = response.text
    mid = re.findall('{"mid":(.*?),',info)      #id
    name = re.findall(',"name":"(.*?)",',info)   #名称
    face = re.findall('"face":"(.*?)",',info)   #头像
    fans = re.findall('"cFans":(.*?),"',info)   #粉丝
    view = re.findall('"cArchiveView":(.*?),"', info)  # 播放
    click = re.findall('"cLike":(.*?)}', info)  # 点赞
    name1 = []
    for i in range (0,40,2):
        name1.append(name[i])
    print(name1)
    #下载到文件
    with open("C:\\Users\\Administrator\\Desktop\\data.csv", "a", newline="") as cf:
        w = csv.writer(cf)
        w.writerow(["name", "face", "fans"])
        for i in range(20) :
            w.writerow([name1[i], face[i], fans[i]])
        cf.close()
bilibilisj()