import pymysql

try:
    print("创建连接！")
    db = pymysql.connect("127.0.0.1","root","123456","size")#连接数据库，参数分别为IP地址、用户名、密码、数据库名
    print("连上了！")
except Exception as e:
    print("连接失败！")
    print(e)
    exit()



cursor = db.cursor()
        # 插入的sql语句
insert_sql = "INSERT INTO jd_size VALUES (4),(3);"
try:
            cursor.execute(insert_sql)
            db.commit()
            print("插入成功！")
except:
            print("插入失败")
            db.rollback()

db.close()

