import requests
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
           'cookie':'_ga=GA1.2.1121954456.1584491004; G_ENABLED_IDPS=google; __cfduid=d0763f26107a5a194fd0c2a9c5281d9b31587220087; JSESSIONID=C7BA7776EBC012A48BDDDC1FD3A607A4; _gid=GA1.2.711535546.1587471902; xf_session=d770e4f4c95e6659d6d06fe29a659c40'}

def getsslink():
    url = 'https://usky.ml/tool/api/free_ssr?page=1&limit=10'
    response = requests.get(url,headers=headers)
    info = response.text
    sslink = re.findall('"sslink":"(.*?)",',info)
    print(info)
    print(sslink)

getsslink()