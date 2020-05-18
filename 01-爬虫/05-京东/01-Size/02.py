import requests
import re
import json
import pymysql


#爬取商品id
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def get_id(key_word,wq):
    #jd_url='https://search.jd.com/Search?keyword=%E5%A5%B3%E6%80%A7%E5%86%85%E8%A1%A3&enc=utf-8&wq=%E5%A5%B3%E6%80%A7nei%27yi&pvid=fafd7af082734ae1a4a6cb674f98b2e4'
    jd_url = 'https://search.jd.com/Search'
    product_ids = []
    # 爬前3页的商品
    j = 51;
    for i in range(17,25,2):
        param = {'keyword': key_word, 'enc': 'utf-8', 'qrst':'1', 'rt':1, 'stop':1, 'vt':2, 'wq':wq, 'page':i, 's':j, 'click':0}
        response = requests.get(jd_url,params = param,headers=headers)
        # 商品id
        ids = re.findall('data-pid="(.*?)"', response.text,re.S)
        product_ids += ids
        if i!= 3:
            j = j+50+i-4;
        else:
            j+=50
    return product_ids

def getSizes(ids):
    Sizes = []
    for id in ids:
        for i in range(0,8):
            url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId='+id+'&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&fold=1'
            response = requests.get(url)
            size = re.findall('"productSize":"(.*?)"',response.text)
            Sizes+=size
    return Sizes

ids = get_id("胸罩","胸罩")
size= getSizes(ids)
print(ids)
print(size)