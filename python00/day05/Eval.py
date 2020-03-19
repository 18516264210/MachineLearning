


# eval
# 将字符串转成代码

# eval只能处理单行代码


f = "1+3/2*7"
print(f)

g = eval(f)
print(g)


# print('张小三，你好呀')
# 张小三，你好呀
# None
h = "print('张小三，你好呀')"
print(h)
i = eval(h)
print(i)


# eval不能转化多行
j = '''
if 5 > 3:
    print('5大于3')
else:
    print('5小于3')
        
'''
# eval不能解析多行代码，只能解析单行代码
# print(eval(j))


print("-------------------exec-------------------")

# 这里面虽然是打印，但是后面会出现一个None,这个None实际上是返回值
# 5大于3
# None
print(exec(j))



k = '''
def foo():
    print("run ...")
    return 1234
    
foo()      
'''

# run ...
# res None
res = exec(k)
print("res",res)