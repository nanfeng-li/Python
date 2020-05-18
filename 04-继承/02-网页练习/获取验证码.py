from selenium import webdriver
import time
import os
import requests

def getQRcodeImgBase64():
    driver = webdriver.Chrome()
    driver.get("https://www.ifeng.com/?source=mozilla")
    time.sleep(10)
    driver.find_element_by_xpath("//*[text()='登录']").click()
    time.sleep(5)
    iframe = driver.find_element_by_css_selector('.box-1pZSPyeN>div>iframe')
    driver.switch_to.frame(iframe)
    url = driver.find_element_by_css_selector(".vloginbox_phone_code>img").get_attribute("src")

#    os.mkdir("C:\\Users\\lgz001\\Desktop\\验证码\\")
#    os.chdir("C:\\Users\\lgz001\\Desktop\\验证码\\")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    im = requests.get(url,headers=headers) # 请求url
    open('1.jpg', 'wb').write(im.content)
    driver.close()
    print("验证码已获取")

getQRcodeImgBase64()