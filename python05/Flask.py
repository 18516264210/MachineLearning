
# 使用flask制作第一个web

# 先安装Flask
# pip install flask flask-stormpath

# 引入Flask
# 这里面的from和import有什么区别么?flask中间包含很多的功能，但是我不需要，我只需要其中的一个功能，所有我就需要使用import 导入其中的Flask
from flask import Flask
import pymysql
import json

#定义app名称
app = Flask(__name__)

@app.route("/get",methods=['GET'])
def index():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='td_xkd')
    # 创建游标
    cursor = conn.cursor()
    cursor.execute("select * from dds_driver_info")
    all_rows = cursor.fetchall()

    # 将数据封装到list中
    drivers = []
    data = {}
    for r in all_rows:
        driver = {}
        driver['tid'] = r[0]
        driver['serial_no'] = r[1]
        driver['driver_name'] = r[2]
        driver['driver_phone'] = r[6]
        driver['id_card_no'] = r[8]
        drivers.append(driver)

    # 将数据封装成json，然后返回到页面
    data['status'] = 0
    data['data'] = drivers
    jsonStr = json.dumps(data)

    cursor.close()
    conn.close()
    return jsonStr




# 启动web
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9999,debug=True)






