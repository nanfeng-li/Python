import requests

"""
1、获取url 网址
2、发送请求
3、提取数据
4、保存
可以加延迟或者多加几个user-agent
Request URL:https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js
Request Method:GET
"""""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
}


def get_id():
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
    res = requests.get(url, headers=headers).json()
    lol_list = res["hero"]
    list1 = []
    for lol in lol_list:
        list1.append(lol["heroId"])
    return list1


def get_skins(lol_lists):
    for i in lol_lists:
        url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js".format(i)
        response = requests.get(url, headers=headers).json()
        skins_list = response["skins"]
        for j in skins_list:
            item = {}
            item["name"] = j["name"]
            item["mainImg"] = j["mainImg"]
            print(item)

            if item["mainImg"]:
                conn = requests.get(item["mainImg"], headers=headers).content
                with open("/" + item["name"] + ".jpg", "wb") as f:
                    f.write(conn)
                    print("正在下载%s" % item["name"])
            else:
                print("没有数据")


lol_lists = get_id()
get_skins(lol_lists)

