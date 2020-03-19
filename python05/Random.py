
# import可以将整个模块都导入
import random


# [10,20]之间的随机数
r = random.randint(10,20);
print(r)


print("---------------------------CharCount字符统计--------------------------------")
# python的wordcount
res = {}
# 读文件
with open(file="wordcount.txt",mode="r",encoding="UTF-8") as f:
    # 去空格
    for char in f.read().replace(' ',''):
        # get(key,默认值),这里的默认值意思就是在获取的时候为获取到数据，那么会给一个默认的返回值
        # res[char] = res.get(char,0) + 1
        # 如果存在+1
        if char in res:
            res[char] = res[char] + 1
        # 如果不存在存一个
        else:
            res[char] = 1

print(res)
# 获取前三名
# 字典没法排序，所以转成list
# 使用sorted函数进行排序
res_list = res.items()
# lambda x:x[1]表示遍历元素，然后获取元素的value。也就是说这里是按照value排序
# reverse=True表示按照从大往小排序,reverse=False表示从小往大排序
print(sorted(res_list,key=lambda x:x[1],reverse=True))
for k,v in sorted(res_list,key=lambda x:x[1],reverse=True)[0:3]:
    print("%s count is %s" % (k,v))



