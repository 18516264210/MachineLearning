
class Yunsuanfu(object):
    '''
    我是文档的注释，我是否可以通过方法获取到呢
    重写object 的方法，类似于java中的方式
    '''
    def __init__(self,name,age):
        '''
        我是方法注释
        :param name:
        :param age:
        '''
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception("age must be int")

    # 重写==方法
    def __eq__(self, other):
        if isinstance(other,Yunsuanfu):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception("The type of object must be Yunsuanfu")

    # 重写加+方法
    def __add__(self, other):
        if isinstance(other,Yunsuanfu):
            return self.age+other.age
        else:
            raise Exception("age must be int")

if __name__ == "__main__":
    y1 = Yunsuanfu("zhangsan",18)
    y2 = Yunsuanfu("lisi",18)
    print(y1==y2)
    print(y1+y2)
    print(y1.__dict__)
    print(y1.__doc__)
