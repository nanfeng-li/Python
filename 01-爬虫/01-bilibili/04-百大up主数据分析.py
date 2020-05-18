import requests
import re
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def bilibili2018():
    url = 'https://www.bilibili.com/blackboard/activity-BPU2018.html'
    response = requests.get(url,headers=headers)
    info = response.text
    name = re.findall('<strong>(.*?)</strong>',info)
    id = re.findall('space.bilibili.com/(.*?)"',info)
    name1 = []
    id1 = []
    for i in name:
        if i not in name1:
            name1.append(i)
    for j in id:
        if j not in id1:
            id1.append(j)
    for k in range(100):
        res = '第'+ str(k) +'位up主：' + name1[k] + '     id:' + id1[k]
        print(res)

def bilibili2019():
    url = 'https://activity.hdslb.com/blackboard/activity17927/static/js/chunk-622a052d.02a6e1f4.js'
    response = requests.get(url, headers=headers)
    info = response.text
    name = re.findall('"name":"(.*?)",',info)
    id = re.findall('"uid":(.*?),',info)
    #for k in range(100):
    #    res = '第'+ str(k) +'位up主：' + name[k] + '     id:' + id[k]
    #    print(res)
    with open("C:\\Users\\Administrator\\Desktop\\2019.csv", "a", newline="") as cf:
        w = csv.writer(cf)
        w.writerow(["name", "id"])
        for k in range(100):
            w.writerow([name[k], id[k]])
        cf.close()

bilibili2019()




