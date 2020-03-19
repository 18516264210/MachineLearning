counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(counter);
print(miles);
print(name);
print("------------------------------------------------")

# Python允许你同时为多个变量赋值。例如：
a = b = c = 1;
print(a);
print(b);
print(c);
print("------------------------------------------------");

# 可以为多个对象指定多个变量。例如：
d, e, f = 1, 2, "john";
print(d);
print(e);
print(f);
print("------------------------------------------------")
#字符串处理
str = 'Hello World!'
print(str)           # 输出完整字符串
print(str[0])        # 输出字符串中的第一个字符
print(str[2:5])      # 输出字符串中第三个至第五个之间的字符串
print(str[2:])       # 输出从第三个字符开始的字符串
print(str * 2)       # 输出字符串两次
print(str + "TEST")   # 输出连接的字符串
print("------------------------------------------------")

#List（列表） 是 Python 中使用最频繁的数据类型。
#列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
#列表用 [ ] 标识，是 python 最通用的复合数据类型。
#列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表
print("------------------------------------------------")

#元组是另一个数据类型，类似于List（列表）。
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组

# 这里对tuple进行了二次赋值，实际打印出来的结果显示并没有替换成功
#tuple[0] = "tomcat";
#print(tuple)

print("------------------------------------------------")
#条件语句
tfflag = 1
if tfflag == 0:
    print("不是我想要的")
    print("进行下一个判断")

elif tfflag == 1:

    print("我要的就是你:1")
else:

    print("你们都不懂我")

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print('welcome boss')    # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称

num = 5
if num == 3:            # 判断num的值，通过==对数据进行比较
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')     # 条件均不成立时输出

print('----------------------------------------------------------')
# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
# 例3：if语句多个条件
num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello
num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine
num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')
    # 输出结果: undefine

print('---------------------------------------------------')
# 可以在同一行的位置上使用if条件判断语句
var = 100
if ( var  == 100 ) : print("变量 var 的值为100")
print("Good bye!")

print('---------------------------------------------------')
# 将多个字符串连接
print('hello python',' i am a good boy',' so are you')
# 将多个值连接，可以是字符串，可以是数字
print('100+200=',100+200)

print('------------------------转义--------------------------')
# \n 表示换行
# \t 表示一个制表符
# \\ 表示 \ 字符本身
# 打印下面一段话，前面有空格,Guide有引号,第二行换行
# Python was started in 1989 by "Guido".
# Python is free and easy to learn.
print('\tPython was started in 1989 by \"Guido\".\n\tPython is free and easy to learn')

print('------------------------变量变更--------------------------')
aa = 'ABC'
bb = aa
aa = 'XYZ'
print(aa)
print(bb)

print('--------------------求等差数列的和-----------------------')
# 等差数列可以定义为每一项与它的前一项的差等于一个常数，可以用变量 x1 表示等差数列的第一项，用 d 表示公差，请计算数列
# 1 4 7 10 13 16 19 ...
# 前 100 项的和。
x1 = 1
d = 3
n = 100
x100 = x1 + n*d
s = n*(x1+x100)/2
print(s)


print('--------------------raw字符串与多行字符串-----------------------')
print(r'\(~_~)/ \(~_~)/')

duohang = '''Line 1
Line 2
Line 3'''
print(duohang)


print('------------------------------字典---------------------------------------')

di={'a':2,'b':4,'c':7}

print(di['a'])
print(di['b'])
print(di['c'])



