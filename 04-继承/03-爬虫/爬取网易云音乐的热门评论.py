import requests
import json
from bs4 import BeautifulSoup


def get_comments(res):
    comments = json.loads(res.text)
    hot_comments = comments['hotComments']
    with open('热门评论.txt', 'w', encoding='utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname'] + ':\n')
            f.write(each['content'] + '\n\n')


def geturl(url):
    headers = {"Referer": "http//music.163.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    # 下面两个参数是网易加密过的，直接在网页元素中复制过来的
    params = "K2HjGyPzWSCz2O772ysQLqvidrQlnnjxpnBh/ZjO8j8FLlHKNxNn+VQyMuztFaxMbUcj4pm98zkF6IpQ7RjIcFGMAbrv+C8DP6MaS5JoEx0MtMcizFfcoysQ0vG9RRTqXP0tRvie+7vgFfcSv1zg1u3zjUPswqWXH7dq9AoRL23cAhG4H9jFcUfUzovMlwXP"
    encSecKey = "ccbe33dd2f440faf537173be8d6b237257d0493faee3708cfbb91ca80ce45c3fa0dfea2af7650d251bd8c140638cae8719906bac1ff379b8c4cc79a1c95e267ab6fc28bc63c78d3e9eff396d4b43a97284b6770ecf429bc209a7954056e2355f81459bdd951ba90da7bb47711556fae4986281fe13c41e89fede0881726731d7"
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    url_id = url.split('=')[1]
    post_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(url_id)
    res = requests.post(post_url, headers=headers, data=data)
    return res


def main():
    url = input("请输入需要下载评论歌曲的网址：")
    res = geturl(url)
    get_comments(res)


if __name__ == "__main__":
    main()