import requests
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url = 'https://www.csdn.net/api/articles?type=new&category=home'
response = requests.get(url,headers=headers)
#print(response.text.encode('utf-8').decode('unicode_escape'))
re = eval("u"+"\'"+response.text+"\'")
print(re)



