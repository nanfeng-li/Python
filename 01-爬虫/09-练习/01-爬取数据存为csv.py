import csv
import os

# 判断文件是否存在
if os.path.exists("C:\\Users\\Administrator\\Desktop\\data.csv"):
    os.remove("C:\\Users\\Administrator\\Desktop\\data.csv")

# 将数据写入文件
with open("C:\\Users\\Administrator\\Desktop\\data.csv", "a", newline="") as cf:
    w = csv.writer(cf)
    w.writerow([1001, "北京"])
    w.writerow([1002, "上海"])
    w.writerow([1003, "广州"])
    cf.close()

# 将数据从文件读出
with open("C:\\Users\\Administrator\\Desktop\\data.csv", "r") as cf:
    d = csv.reader(cf)
    for row in d:
        print(row)