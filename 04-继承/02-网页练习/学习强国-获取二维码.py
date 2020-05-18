from selenium import webdriver
import time
import os
def getQRcodeImgBase64():
    driver = webdriver.Firefox()
    driver.get("https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/index.html")
    time.sleep(10)
    QRcodeTemp = driver.find_elements_by_tag_name('iframe')[2]

    driver.switch_to.frame(QRcodeTemp)
    a =driver.find_element_by_css_selector(".login_content>.login_body>.login_qrcode>.login_qrcode_content>img").get_attribute("src")
    driver.close()
    return a


def imgio(binary_img_data):
    # 创建文件夹
    os.mkdir("C:\\Users\\lgz001\\Desktop\\二维码\\")
    # 进入创建好的文件夹
    os.chdir("C:\\Users\\lgz001\\Desktop\\二维码\\")
    with open("QRcode.png","wb+") as imgfile:
        imgfile.write(binary_img_data)
        print ("二维码已获取")

def start():
    import base64
    Base64Data = getQRcodeImgBase64()
    data = Base64Data.split(",")[-1]
    binary_img_data = base64.b64decode(data)
    imgio(binary_img_data)

start()
