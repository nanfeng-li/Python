import pandas as pd
import requests
import re
import time

data_list = []

for i in range(1,300,1):
    print("正在爬取第" + str(i) + "页")
    url = first + str(i) + last
    headers ={
        # 用的哪个浏览器
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        # 从哪个页面发出的数据申请，每个网站可能略有不同
        'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.744840c2FKDkFG&id=43751299764&skuId=4493124079453&areaId=421300&user_id=2380958892&cat_id=2&is_b=1&rn=388ceadeefb8d85e5bae2d83bd0b732a',
        # 哪个用户想要看数据，是游客还是注册用户,建议使用登录后的cookie
        'cookie': 'tk_trace=1; cna=qzxtFlkIdkICARsvgIh8ftNm; t=972672ef4a0555634bb4c53147d9c209; _tb_token_=f9ed83467e7ab; cookie2=11c397b08781b52815002215ea5d1ad4; dnk=huang%5Cu81F3%5Cu5C0A; tracknick=huang%5Cu81F3%5Cu5C0A; lid=huang%E8%87%B3%E5%B0%8A; lgc=huang%5Cu81F3%5Cu5C0A; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&existShop=false&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=UoTUP2D4F2IHjA%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1; uc3=id2=UU8BrRJJcs7Z0Q%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dBxd9hhEzOWS%2BU9Dk%3D&nk2=CzhMCY1UcRnL; _l_g_=Ug%3D%3D; uc4=id4=0%40U22GV4QHIgHvC14BqrCleMrzYb3K&nk4=0%40CX8JzNJ900MInLAoQ2Z33x1zsSo%3D; unb=2791663324; cookie1=BxeNCqlvVZOUgnKrsmThRXrLiXfQF7m%2FKvrURubODpk%3D; login=true; cookie17=UU8BrRJJcs7Z0Q%3D%3D; _nk_=huang%5Cu81F3%5Cu5C0A; sgcookie=E53NoUsJWtrYT7Pyx14Px; sg=%E5%B0%8A41; csg=8d6d2aae; enc=VZMEO%2BOI3U59DBFwyF9LE3kQNM84gfIKeZFLokEQSzC5TubpmVCJlS8olhYmgHiBe15Rvd8rsOeqeC1Em9GfWA%3D%3D; l=dBLKMV6rQcVJihfaBOfgSVrsTkQ9UIRb8sPrQGutMICP9ZCwNsyFWZ4Kb-8eCnGVHsMvR3oGfmN0BDTHXyIVokb4d_BkdlkmndC..; isg=BK2tcrfNj3CNMWubo5GaxlajvEknCuHcPbxLgO-yO8QhZswYt1ujrPVwUDqAZvmU'
    }
    try:
        data = requests.get(url,headers = headers).text
        time.sleep(10)
        result = re.findall('rateContent":"(.*?)"fromMall"',data)
        data_list.extend(result)
    except:
        print("本页爬取失败")
df = pd.DataFrame()
df["评论"] = data_list
df.to_excel("评论_汇总.xlsx")
