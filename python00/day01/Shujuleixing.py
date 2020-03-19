"""
基本数据类型：数字(整形int，长整形long，浮点float)，字符串(文本str，字节bytes)，布尔

数据集合：列表list，元组tuple，字典dict，集合set

int:
    在32位的机器上，寻址范围-2~31 到 2~31-1
    在64位的机器上，寻址范围-2~63 到 2~63-1

long（python3之后没有long类型）:
    可以无限大

"""



# 数据类型

age = 12
print(type(age))
print(isinstance(age,int))
print(age)
print("------------------------------------------------")

# python3之后没有long类型
money = 999999999999999999
print(type(money))
print(isinstance(money,int))
print(money)
print("------------------------------------------------")

# 2的63次方
money1 = 2**63
print(type(money1))
print(isinstance(money1,int))
print(money1)
print("------------------------------------------------")

name = "张三"
print(type(name))
print(isinstance(name,int))
print(name)
print("------------------------------------------------")

# 三个单引号可以跨行，双引号没法跨行
mydan = 'my name is li'
print(mydan)
myname = "my name is t,I'm 18"
print(myname)
myshi = '''
        i'm 18,
        i have a dream
        '''
print(myshi)

print("------------------------------------------------")
# 字符串拼接，不能和数字进行拼接
dange = "a"
chongfu = dange*10
print(chongfu)
