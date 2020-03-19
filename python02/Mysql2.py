import pymysql
import time
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='python')
# 创建游标
cursor = conn.cursor()

# 插入数据
create_time = time.strftime('%Y-%m-%d %H:%M:%S')
print("create_time:",create_time)
#Sql 插入语句
sql = "insert into user_info(user_name,password,age,create_time) " \
      "VALUES ('%s','%s','%s','%s')" \
      %("王五","123456",39,create_time)
try:
    #执行sql
    print("==执行插入==")
    tt = cursor.execute(sql)
    print(tt)
    conn.commit()
    print("==插入完成==")
except UnicodeEncodeError as e :
    #发生错误时回滚
    print(e)
    conn.rollback()
conn.close()