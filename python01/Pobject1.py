class Pobject1:
    empCount = 0

    def __init__(self):
        print("=====1")
        # 什么也不干，使用pass
        pass

    # 有参数的构造函数
    def __init__(self, name, salary):
        print("=====2")
        self.name = name
        self.salary = salary
        Pobject1.empCount += 1

    # 自定义方法
    def displayCount(self):
        print("Total Employee %d" % Pobject1.empCount)
    # 自定义方法
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

    def displayPrint(self):
        print("我是A")
# main方法
if __name__ == '__main__':
    p = Pobject1('张三',8000)
    p.displayCount()
    p.displayEmployee()
    print("=========================1")
    # p2 = Pobject1()
    # p2.displayPrint()
    print("=========================2")
