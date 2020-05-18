import cx_Oracle

db = cx_Oracle.connect('SYSTEM', '123456', '127.0.0.1:1521/XE')

cr = db.cursor()
# 小时粒度人流信息表
sql = "insert into tb_1 values " \
      "(8,'jd',20)"
cr.execute(sql)
db.commit()
#rs = cr.fetchall()
#old_data = pd.DataFrame(rs)