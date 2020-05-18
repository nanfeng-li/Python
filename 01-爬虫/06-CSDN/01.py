import requests
import re
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def get_title():
    url = 'https://www.csdn.net/api/articles?type=new&category=home'
    response = requests.post(url,headers=headers)
    a = eval("u" + "\'" + response.text + "\'")
    print(a)
    title = re.findall('"title":"(.*?)",',a)
    views =re.findall('"views":(.*?),',a)
    comments = re.findall('"comments":(.*?),', a)
    digg = re.findall('"digg":(.*?),', a)
    nickname = re.findall('"nickname":(.*?),', a)
    # print(title)
    # print(views)
    # print(comments)
    # print(digg)
    # print(nickname)
    i = len(title)
    #print(i)


    for j in range(i):
        x = '标题：'+ title[j] + '  查看：' + views[j] + '  评论：' + comments[j] +'  点赞：'+ digg[j] +'  作者：' + nickname[j]
        print(x)

    df = pd.DataFrame()
    df["评论"] = title
    df.to_excel("评论_汇总.xlsx")
g=0
while g < 1:
    get_title()
    g+=1
