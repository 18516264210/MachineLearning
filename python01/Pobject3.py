# 方法的定义跟属性一样，可以按照下划线对其访问权限进行控制
class Pobject3:
    # 函数和方法
    # 函数可以直接通过函数名调用，而方法需要和对象在一起使用
    def add(self):
        print('add:--我是一个方法--')

    # 一个下划线只是一个约定，所以可以访问
    def _del(self):
        print("我是删除方法")
        pass

    # 两个下划线，名称会被强转成其他名称，所以需要通过其他途径调用
    def __upd(self):
        print("我是修改方法")
        pass

# 万物皆对象，方法也是对象的一个属性
if __name__ == '__main__':
    p = Pobject3()
    p.add()
    p.add = 'add:--你才不是方法呢，你是数字123--'
    print(p.add)

    # 同样的，在访问方法的时候，也是需要通过dir看看方法变成了什么样子
    print(dir(p))
    # 这里算法没有提示，但是可以调用
    p._del()
    p._Pobject3__upd()