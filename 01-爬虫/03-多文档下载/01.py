import urllib.request
import os

xl = list(range(153800,156400)) #1567 #196
yl = list(range(293712,295237)) #2952 #370
num=0
i = 0
for x in xl:
    os.mkdir("G:\\TP\\" + str(xl[i]))
    # 进入创建好的文件夹
    os.chdir("G:\\TP\\" + str(xl[i]))
    i += 1
    for y in yl:
        num=num+1
        url = 'https://pnr.sz.gov.cn/d-suplicmap/tileszmap_1/rest/services/SZMAP_BASEMAP_GKDL/MapServer/tile/10/' + str(
            y) + '/' + str(x)
        HEADERS = {
            'Referer': 'http://pnr.sz.gov.cn/ywzy/qt/bddj/',
            'Sec-Fetch-Dest': 'iframe',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }
        request = urllib.request.Request(url, headers=HEADERS)
        r_response = urllib.request.urlopen(request)
        r = r_response.read()
        #保存为png文件
        open(str(y)+'_'+str(x)+'.jpg', 'wb').write(r)
        print('第'+str(num)+'幅')
        y=y+1
    x=x+1
    y=yl[0]
