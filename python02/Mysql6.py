import pymysql
import time
import random
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='python')
# 创建游标
cursor = conn.cursor()

# 批量插入
# 与Mysql5.py中python提供的批量插入功能，这里使用逐条插入(批量提交)，看一下效果怎么样
# 注意这里一定要使用批量提交，如果将commit放在for循环，那就惨了。亲测插入1000条数据，用时42秒。
# 12:34 , 12:49
# 实际结果表明逐条插入用时15秒，不批量插入慢了一倍多


create_time = time.strftime('%Y-%m-%d %H:%M:%S')
print("create_time:",create_time)

params = []
for i in range(100000):
    param = ("username"+str(i),"123456",random.choice(range(100)),create_time)
    params.append(param)

start_time = time.strftime("%H:%M:%S")
try:
    for p in params:
        sql = "insert into user_info (user_name,password,age,create_time) values  (%s,%s,%s,%s)"
        tt = cursor.execute(sql,p)
        # 提交千万不能放在这里
        # conn.commit()
    print("----------批量提交----------")
    conn.commit()
except Exception as e:
    print("插入出现异常")
    print(e)
    # 出现异常回滚
    conn.rollback()
finally:
    cursor.close()
    conn.close()
end_time = time.strftime("%H:%M:%S")
print(start_time,",",end_time)

