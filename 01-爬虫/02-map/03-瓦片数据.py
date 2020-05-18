import urllib.request

#此处经纬度范围可根据具体要求调整
#本例范围为成都
xmin=51695
xmax=51745
ymin=26870
ymax=26920
x=xmin
y=ymin
num=0
while(x<xmax):
    while(y<ymax):
        num=num+1
        url = 'https://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Gray_OnlySymbol/MapServer/tile/16/'+str(y)+'/'+str(x)+'?blankTile=false'
        #'url'中的'Gray_OnlySymbol'为地图类型，可根据需要调整
        #'url'中的'16'为图幅大小，可根据需要调整
        HEADERS = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,en-US;q=0.7,en;q=0.3',
        'Connection':'keep-alive',
    'Cookie':'Hm_lvt_ca4d6c93ba95a519be60addfd546ac72=1533781615,1533806950,1533807108,1533807258',
        'Host':'thematic.geoq.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        request = urllib.request.Request(url, headers=HEADERS)
        r_response = urllib.request.urlopen(request)
        r=r_response.read()
        #保存为png文件
        with open('C:\\Users\\Administrator\\Desktop\\TP\\'+str(y)+'_'+str(x)+'.png', 'wb') as f:
            f.write(r)
            print('第'+str(num)+'幅')
        y=y+1
    x=x+1
    y=ymin