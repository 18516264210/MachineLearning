
# 需要下载
import requests
import json
# pip install request -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 通过requests爬取新浪网的一个网页

# 这里获取的网页都是HTML格式的
# newsUrl = "http://www.baidu.com"
# result = requests.get(newsUrl,verify=False)
# result.encoding = "UTF-8"
# print(result.text)

# 对HTML格式的数据进行解析

print("=================================================request post==========================================================")

xiakesongurl1 = "http://localhost:9080/customer_1.1/u/business/ipos/dorders"
xiakesongurl2 = "http://localhost:9080/customer_1.1/u/business/ipos/oastm"
xiakesongurl3 = "http://localhost:9080/customer_1.1/u/business/ipos/stupt"
body={"shopId":"10028932","orderId":"123459","src":"02","type":"1","timestamp":"2019-04-24 16:33:00"}
# 这里的body由于是json，所以需要使用json进行转换。或者将body转换为字符串，即在前后加单引号也可以实现
data = {"channel":"1030","version":"1.2.0","body":json.dumps(body),"sign":"123456789"}
headers = {'content-type': "application/json"}
appkey = "u2967a4edf304275942f153254853c14"
# 转换后的data数据
# {'channel': '1030', 'version': '1.2.0', 'body': '{"shopId": "10028932", "orderId": "123459", "timestamp": "2019-04-24 16:33:00"}', 'sign': '123456789'}
# 未转换的data数据
# {'channel': '1030', 'version': '1.2.0', 'body': {'shopId': '10028932', 'orderId': '123459', 'timestamp': '2019-04-24 16:33:00'}, 'sign': '123456789'}
print(data)
count = 20
while count>0:
    response = requests.post(xiakesongurl3,data=data)
    count = count-1
    print(response.status_code)
    print(response.text)
else:
    print("=================执行结束")

