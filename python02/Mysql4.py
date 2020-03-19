import pymysql
import time
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='python')
# 创建游标
cursor = conn.cursor()

# 防止sql注入

create_time = time.strftime('%Y-%m-%d %H:%M:%S')
print("create_time:",create_time)

try:
    # 这里的%s不能加单引号
    sql = "insert into user_info (user_name,password,age,create_time) values  (%s,%s,%s,%s)"
    values = ("赵六","123456",13,create_time)
    tt = cursor.execute(sql,values)
    print(tt)
    conn.commit()
except Exception as e:
    print("插入出现异常")
    print(e)
    conn.rollback()
conn.close()