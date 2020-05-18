import pymysql


def create_db_link():
    #创建数据连接
    try:
        print("创建连接！")
        #连接数据库，connect的参数分别为IP地址、用户名、密码、数据库名（要和自己的数据库对上）
        db = pymysql.connect("localhost","root","123456","new_schema")
        print("连上了！")
    except Exception as e:
        print("连接失败！")
        print(e)
        exit()
    """
    主要代码
    """
    db.close()

def create_tb(db):
    #使用cursor()方法操作游标

    cursor = db.cursor()

    #如果tb_name存在，则删除
    cursor.execute("DROP TABLE IF EXISTS tb_1")
    #执行建表操作
    create_sql = "CREATE TABLE tb_1 (ID INT NOT NULL, \
                       Name CHAR(8),\
                       Grade INT )" #建表sql语句
    cursor.execute(create_sql)

def write_tb(db):
    #使用cursor()方法获得游标
    cursor = db.cursor()
    #插入的sql语句
    insert_sql="INSERT INTO tb_1 \
         VALUES (1, '张三', 70),\
                (2, '李四', 80),\
                (3, '王五', 90),\
                (4, '许六', 80),\
                (5, '何七', 70),\
                (6, '吕八', 66),\
                (7, '龙九', 100)"
    try:
        cursor.execute(insert_sql)
        db.commit()
        print("插入成功！")
    except:
        print("插入失败")
        db.rollback()

def query_db(db):
    #使用cursor()方法获取操作游标
    cursor = db.cursor()
    query_sql="SELECT * FROM tb_1"
    try:
        cursor.execute(query_sql)
        #获取所有数据
        results = cursor.fetchall()
        #获得属性名称和长度（list）
        fields = cursor.description
        n = len(fields)#
        print('\t'.join([str(i[0]) for i in fields]))
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            print(str(ID)+'\t'+str(Name)+'\t'+str(Grade))

    except:
        print("获取数据失败")

def update_tb(db):
    #使用cursor方法获取操作游标
    cursor = db.cursor()
    update_sql = "UPDATE tb_1 SET Grade=Grade+5 WHERE Grade=80"
    try:
        #执行SQL语句
        cursor.execute(update_sql)
        #提交到数据库执行
        db.commit()#数据的改变需要执行这个命令
    except:
        print("更新失败！")
        #发生错误时回滚
        db.rollback()

def delete_db(db):
    #删除数据
    cursor = db.cursor()
    delete_sql = "DELETE FROM tb_1 WHERE Grade=66"
    #SQL删除语句
    try:
        cursor.execute(delete_sql)
        db.commit()#提交数据库执行删除
    except:
        print("删除数据失败！")
        db.rollback()#有错误时进行回滚

db = pymysql.connect("localhost","root","123456","new_schema")
delete_db(db)
db.close()
