#bilibili关键字爬虫存放csv文件
#__author:Jiangtao
#data:2020/3/25
import pandas as pd
import requests
import re
import random
import json
import time
from bs4 import BeautifulSoup
import lxml

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]
key = input('输入关键字:')
#获取cid与bvid
for i in range(1, 51):
    header2 = {'User-Agent': random.choice(user_agent),
               'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
               'Connection': 'keep-alive',
               'Host': 'api.bilibili.com',
               'Origin': 'https://www.bilibili.com',
               'Referer': 'https://www.bilibili.com/video',
               'Sec-Fetch-Dest': 'empty',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Site': 'same-site'
               }
    header = {'User-Agent': random.choice(user_agent)}
    url = 'https://search.bilibili.com/all?keyword='+str(key)+'&page=' + str(i)
    r = requests.get(url=url, headers=header, timeout=30)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, "lxml")
    s1 = soup.findAll('a', {'class': 'title'})
    for c in s1:
        try:
            bvid = re.findall("BV[0-9a-zA-Z]*", c.get("href"))
            param1 = {"bvid": bvid}
            if len(param1['bvid'])==0:
                pass
                continue
            else:
                # print(param1['bvid'])
                url1 = 'https://api.bilibili.com/x/player/pagelist?'
                r1 = requests.get(url=url1, params=param1, headers=header)
                r1.encoding = "utf-8"
                str_data = r1.content
                str_json = str_data
                # print(str_json)
                json_Info = json.loads(str_json)
                json_Info = json_Info['data']
                cid = json_Info[0]['cid']
                # print(cid)

    #视频内容提取
                param2 = {"cid": cid, "bvid": bvid}
                url2 = "https://api.bilibili.com/x/web-interface/view?"
                r2 = requests.get(url=url2, headers=header2, params=param2, timeout=30)
                r2.encoding='utf-8'
                str_data1 = r2.content
                str_json1 = str_data1
                json_Info1 = json.loads(str_json1)
                #data数据
                json_Info1=json_Info1['data']
                bvidnum=json_Info1['bvid']
                aid=json_Info1['aid']
                tname=json_Info1['tname']
                title=json_Info1['title']
                desc=json_Info1['desc']
    #             print(title, tname, aid, desc,)

                # #own数据
                own=json_Info1['owner']
                name=own['name']
    #             print(name)

                # #stat数据
                stat=json_Info1['stat']
                view=stat['view']
                danmu=stat['danmaku']
                reply=stat['reply']
                favorite=stat['favorite']
                coin=stat['coin']
                share=stat['share']
                like=stat['like']
                dynamic=json_Info1['dynamic']
    #             print(view,danmu,reply,favorite,coin,share,like,dynamic)
                print({'标题': title,'视频简介':desc,'分类':tname,'bv号':bvidnum,'av号': aid, '点赞': like, "硬币": coin, "收藏": favorite, "分享": share,'up主':name,'标签':dynamic})
                Data = pd.DataFrame({'标题': title,'视频简介':desc,'分类':tname,'bv号':bvidnum,'av号': aid, '点赞': like, "硬币": coin, "收藏": favorite, "分享": share,'up主':name,'标签':[dynamic]})
                Data.to_csv('bilibili视频数据.csv', mode='a', header=False, index=False, sep=',', encoding='utf-8-sig')
                time.sleep(1)
        except:
            print("读取有误")
        continue
