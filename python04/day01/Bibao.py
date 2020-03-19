# _*_coding:utf-8_*_

# 闭包
# 这里会有一个问题：在执行完func1()之后，func1中的局部变量就会释放，理论上讲执行f()是获取不到n的值的，那么为什么会获取到值了呢？？？
# 这就是闭包的概念


n = 5
def func1():
    n = 10
    def func2():
        print("func2:",n)

    return func2

# 返回func2的内存地址
f = func1()
print(f)

# 执行func2，结果：func2: 10
f()









