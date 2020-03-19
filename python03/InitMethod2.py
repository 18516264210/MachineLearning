# 运行结果显示 程序在运行的时候会先调用__new__方法，创建一个对象
# 在运行__new__方法的时候一定要返回，不然无法进行__init__的调用

class InitMethod2:

    def __init__(self, name, age):
        print("调用__init__")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("调用__new__ %s" % cls)
        # 这里一定要返回，不然无法进行初始化
        return super(InitMethod2,cls).__new__(cls)

if __name__ == "__main__":
    i = InitMethod2("zhangsan",16)
    print(i.__dict__)