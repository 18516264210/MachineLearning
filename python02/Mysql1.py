import pymysql

# 有些python库的原因导致pymysql无法进行install，可以使用下面的命令进行
# pip install pymysql -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# pip存在于python安装包下，如果配置了环境变量，可以在命令行直接使用，如果使用的是Anaconda，该命令在Scripts包下

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='td_xkd')
# 创建游标
cursor = conn.cursor()
cursor.execute("select * from dds_driver_info")

print("-----------------------获取第一条数据--------------------------")
# 获取第一行数据
row_1 = cursor.fetchone()
print(row_1)

print("-----------------------获取前几行的数据----------------------")
# 获取前三行数据
rows_3 = cursor.fetchmany(3);

print("-----------------------不同的遍历方式------------------------")
for data in rows_3:
    print(data)

print("-----------------------枚举类型遍历--------------------------")
# 前面会有索引
for data in enumerate(rows_3):
    print(data)

print("-----------------------枚举类型带索引------------------------")
for index,data in enumerate(rows_3):
    print(index,":",data)

print("-----------------------range类型遍历-------------------------")
for index in range(len(rows_3)):
    print(index,":",rows_3[index])

print("-----------------------iter类型遍历--------------------------")
for data in iter(rows_3):
    print(data)

print("-----------------------获取所有的数据--------------------------")
# 获取所有的信息
rows_all = cursor.fetchall()
for data in rows_all:
    print(data)


conn.close()