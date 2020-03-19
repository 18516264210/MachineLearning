# _*_coding:utf-8_*_

# 作用域的查找顺序

# 没有变量，会从内到外

n = 10

def func1():
    n = 20
    print("func1:",n)

    def func2():
        n = 30
        print("func2:",n)

        def func3():
            print("func3:",n)

        func3()

    func2()

func1()