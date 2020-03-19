import pymysql
import time
import random
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='python')
# 创建游标
cursor = conn.cursor()

# 批量插入
# 这里进行了10w条数据的批量插入，实际用时6秒
# 04:25 , 04:31
# 结果显示非常快

create_time = time.strftime('%Y-%m-%d %H:%M:%S')
print("create_time:",create_time)

params = []
for i in range(100000):
    param = ("username"+str(i),"123456",random.choice(range(100)),create_time)
    params.append(param)

start_time = time.strftime("%M:%S")
try:
    sql = "insert into user_info (user_name,password,age,create_time) values  (%s,%s,%s,%s)"
    tt = cursor.executemany(sql,params)
    conn.commit()
except Exception as e:
    print("插入出现异常")
    print(e)
    # 出现异常回滚
    conn.rollback()
finally:
    cursor.close()
    conn.close()
end_time = time.strftime("%M:%S")
print(start_time,",",end_time)

