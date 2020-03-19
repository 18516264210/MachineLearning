# 介绍类属性值和类方法
class Pobject4:
    hbbb = "plis"
    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight


    # 相当于java中被static修饰
    @classmethod
    def get_classmethod(cls):
        return cls.hbbb

    # 相当于java中被static修饰
    @property
    def get_weight(self):
        return self.__weight

    def get_name(self):
        return self.name

    def self_introduction(self):
        # 使用占位符
        print("My name is %s \nI am %s years old"% (self.name,self._age))

if __name__ == "__main__":
    p = Pobject4("张三",8,80)
    print(dir(p))
    print(p.__dict__)

    # 类直接调用方法
    print(Pobject4.get_classmethod())
    # 不能直接调用
    # Pobject4.self_introduction()


    # 类直接调用属性。这里相当于java中的封装，将weight定义为私有变量，然后提供一个方法入口调用
    print(Pobject4.get_weight)
    # 也可以通过对象调用
    print(p.get_classmethod())
    # 没有使用@classmethod修饰，必须使用对象调用。不能直接使用类调用
    p.self_introduction()
