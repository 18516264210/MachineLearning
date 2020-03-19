
# 嵌套函数
# 在函数内部定义函数(多个)

def function1():
    print("我是函数function1")

    def function2():
        print("我是函数function2")

    # 在函数function1()中调用function2()
    function2()

# 调用function1()
function1()


print("-----------------------------------------1")

age = 18
def function3():
    age = 19
    print(age)

    def function4():
        age = 20
        print(age)

    function4()
    print(age)

# 一层一层的向外寻找变量
function3()
print(age)


print("-----------------------------------------2")

name = "zhangsan"
def function5():
    def function6():
        print(name)

    name = "lisi"
    function6()
# 一层一层的向外寻找变量，执行function6()的时候name已经定义了，所以结果是lisi
function5()


print("-----------------------------------------3")

passw = "123456"
def function7():
    def function8():
        print(passw)

    function8()
    # 这个地方注释掉，就可以正常执行，为什么加上就会报错呢
    passw = "12345697"
# 执行会报错
function7()