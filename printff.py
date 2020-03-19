
class Printf:


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def new_print(self):
        print("=====name:%s=====age:%s=====" % (self.name,self.age))
        print("=====name:",self.name,"=====age:",self.age,"=====")

# lambda表达式，用于简单的函数，复杂的函数不要用
func1 = lambda x,y : x+y
print(func1(1,2))
# 如果输入参数是2的倍数，则返回该参数，否则返回输入错误
func2 = lambda x : x if x % 2 == 0 else "输入错误"
print(func2(2))
# filter对遍历的集合进行过滤。为什么这里不返回0呢？
print(list(filter(lambda x : x if x % 2 == 0 else "", range(20))))

