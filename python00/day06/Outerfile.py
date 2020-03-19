class Annimal(object):

    # def __init__(self):
    #     self = self
    #     print("=====无参构造")

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("=========")


    def inner_method(self):
        print("我是内部方法")

    def print_attribute(self,name,age):
        print("name:%s=======age:%s")%name,age