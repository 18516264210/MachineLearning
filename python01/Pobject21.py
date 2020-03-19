# coding:utf-8

'this is a model'

# 这里指定的变量。有啥意义呢？可以作为一个模块的作者
__author__="zhangan"

print(__author__)


class Project:
    name = "zhangsan"
    _age = 10
    __weight = 120

    def printInfo(self):
        # 这里可以引用私有变量，对象内部自己访问自己
        str = "name:%s,age:%s,weight:%s" % (self.name,self._age,self.__weight)
        print(str)

if __name__ == "__main__":
    p = Project()
    print(dir(p))
    # 这里无法直接通过p.的方式来访问私有变量。通过dir的方式查看私有变量的变形
    # 这里不会给到提示，但是调用
    print(p._Project__weight)