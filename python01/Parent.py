# 类的继承，定义父类
class Parent(object):
    pname = "parent"

    def __init__(self):
        print("调用无参构造")
        pass

    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight

    def eat(self,food):
        print(food)

    # 相当于java中被static修饰
    @classmethod
    def get_classmethod(cls):
        return cls.pname

    # 相当于java中被static修饰。修饰完后，通过对象为啥不能调用呢？
    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        # 使用占位符
        print("=>【parent】 My name is %s \nI am %s years old"% (self.name,self._age))

if __name__=="__main__":
    # 静态方法调用
    get_classmethod = Parent.get_classmethod()
    print(get_classmethod)

    a = Parent("zhangsan",13,20)
    a.eat("水果")

    www = a.get_weight();
    print(www)
    # 静态属性的调用
    weight2 = Parent.get_weight;
    print(weight2)