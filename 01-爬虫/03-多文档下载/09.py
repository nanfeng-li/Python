import urllib.request

#此处经纬度范围可根据具体要求调整
#本例范围为成都
Y = list(range(1468,1476))
X = list(range(768,781))
x=X[0]
y=Y[0]
num=0
while(x<X[-1]):
    while(y<Y[-1]):
        num=num+1
        url = 'https://pnr.sz.gov.cn/d-suplicmap/tileszmap_1/rest/services/SZMAP_BASEMAP_GKDL/MapServer/tile/3/'+str(y)+'/'+str(x)
        #'url'中的'Gray_OnlySymbol'为地图类型，可根据需要调整
        #'url'中的'16'为图幅大小，可根据需要调整
        HEADERS = {
        'Referer':'http://pnr.sz.gov.cn/ywzy/qt/bddj/',
        'Sec-Fetch-Dest':'iframe',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }
        request = urllib.request.Request(url, headers=HEADERS)
        r_response = urllib.request.urlopen(request)
        r=r_response.read()
        #保存为png文件
        with open('G:\\map\\'+str(y)+'_'+str(x)+'.jpg', 'wb') as f:
            f.write(r)
            print('第'+str(num)+'幅')
        y=y+1
    x=x+1
    y=Y[0]