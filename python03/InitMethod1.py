# 运行结果显示 程序在运行的时候会先调用__new__方法，创建一个对象
# 然后再由__init__对对象进行初始化
# __new__在创建一个实例的过程中必定会被调用,但__init__就不一定。

class InitMethod1:
    '''
    一个类只能有一个构造方法
    '''
    def __init__(self,name, age,**kwargs):
        print("调用__init__")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        '''
        cls表示当前正在实例化的类
        :param args:创建对象传递的参数，这里接收的是一个元祖，如果有多个参数的话，会被打包。
        :param kwargs:接收的是字典类型的数据。具体参数的传递，详见python00/day04/Bianliang.py
        :return:
        '''
        print("调用__new__ %s" % cls)
        print("args:",args)
        print("kwargs:",kwargs)
        # 这里调用的实际是object的__new__方法
        return super(InitMethod1, cls).__new__(cls)

if __name__ == "__main__":
    ii = InitMethod1()
    print("========================================================================================")
    i = InitMethod1("zhangsan",16,passwd="123456")
    print(i.__dict__)