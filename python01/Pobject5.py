
# 类的继承
# python3后所有的类默认进程object，有点儿类似于java，不需要在所有的类后面都添加一个括号，然后写上object
# 但是如果需要继承其他的类，还是需要这样写的
# 调用父类的方法可以使用super()

# 引入的时候，可能需要包的概念，但是无关紧要。import引入的是类，前面from的是文件
from python01.Parent import Parent


class Pobject5(Parent):
    sname = "son"

    def eatt(self,food):
        super(Pobject5, self).eat(food)

    def __init__(self):
        pass

    def __init__(self,name,age,weight,language):
        super(Pobject5, self).__init__(name,age,weight)
        self.language=language


if __name__ == "__main__":
    p = Pobject5("zhangsan",8,80,"english")
    print(dir(p))
    print(p.__dict__)
    # 种类
    print(type(p))

    # 判断父类
    print(isinstance(p,Parent))

    print("=========================================")
    # python中只能有一个构造函数，不能使用无参数的
    p = Pobject5("zhangsan",8,80,"english")
    p.eatt("apple")