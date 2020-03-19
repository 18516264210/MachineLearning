
from python01.Parent import Parent

# 多态
class Pobject6(Parent):
    sname = "son"

    def __init__(self,name,age,weight,language):
        super(Pobject6,self).__init__(name,age,weight)
        self.language=language

    def self_introduction(self):
        print("=>【son】 My name is %s \nI am %s years old"% (self.name,self._age))


# 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
# 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。
# 也就是说，每个对象可以用自己的方式去响应共同的消息。
# 所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数
def introduce(pobject):
    # 这里不管传递的是子类还是父类，都可以直接调用self_introduction方法，返回不同的结果
    # if isinstance(pobject,Parent):
    #     pobject.self_introduction()

    # 这里实际上无需判断是否是父类，还是子类
    pobject.self_introduction()


if __name__ == "__main__":
    ps = Pobject6("zhangsan",8,80,"english")
    pp = Parent("lisi",18,90)
    introduce(ps)
    introduce(pp)