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
    sql = "select * from user_info WHERE user_name=%s and password=%s"
    values = ("张三","123456")
    cursor.execute(sql,values)
    row_1 = cursor.fetchone();
    print(row_1)
except Exception as e:
    print(e)
    conn.rollback()
conn.close()