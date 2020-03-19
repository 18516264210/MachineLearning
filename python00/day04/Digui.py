
# 递归
import sys

# 系统默认的递归次数
print("递归的最大次数：",sys.getrecursionlimit())
# 设置系统的递归次数
sys.setrecursionlimit(1500)

def digui(x):
    if x<10000:
        print("x:",x)
        digui(x+100)
    else:
        print(x)
        print("我被执行了")

    return x

# 为什么结果是99呢？
val = digui(99)
print(val)
# 递归是基于栈数据结构实现的，也就是说每一次递归，都会创建新的不同的栈帧 ，一层方法执行完毕，那么内存就会释放掉

print("------------------------递归二------------------------")

name = "abc|"
def digui2(x):
    global name
    name += x
    if len(name) < 100:
        digui2(name)

    return name

val = digui2("abc|")
print(val)


print("------------------------递归三，算阶乘------------------------")
# 递归调用，尽量从1个数据开始算，否则容易陷入逻辑问题
def factorial(n):
    # 在这里为什么要返回1，因为在递归到1的时候，需要返回一个值，那么就是1
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))


