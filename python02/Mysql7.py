import pymysql
import time
import random
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='python')
# 创建游标
cursor = conn.cursor()

# 修改数据

create_time = time.strftime('%Y-%m-%d %H:%M:%S')
print("create_time:",create_time)

try:
    sql = "update user_info set password = %s,updater_name = %s,update_time = %s WHERE id = %s"
    params = ("123456","admin",create_time,2101);
    cursor.execute(sql,params)

    print("----------更新提交----------")
    conn.commit()
except Exception as e:
    print("插入出现异常")
    print(e)
    # 出现异常回滚
    conn.rollback()
finally:
    cursor.close()
    conn.close()

