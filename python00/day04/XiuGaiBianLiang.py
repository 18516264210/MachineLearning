
# 修改变量

name = "zhangsan"
def update_var1():
    # 局部变量
    name = "lisi"
    print("name:",name,id(name))

update_var1()
print("name:",name,id(name))

# 执行结果：
# name: lisi 30827664
# name: zhangsan 34825264
# 也就是说实际上函数内部的name和函数外部的name并不是一个name，而是两个不同的name

print("---------------------------------")

name = "zhangsan"
def update_var2():
    # 局部变量
    print("name:",name,id(name))

update_var2()
print("name:",name,id(name))

# 执行结果：
# name: zhangsan 34824560
# name: zhangsan 34824560
# 函数在执行的时候先从函数内部搜索各参数，如果函数内部没有，就会搜索函数外部的参数
# 局部变量随着方法的调用而生成，随着方法的执行完成被销毁


print("----------------列表变量操作-----------------")

lst = ["zhangsan","lisi","wangwu"]
def change_list1():
    lst = ["zhangsan","lisi","zhaoliu"]
    print(lst)

change_list1()
print(lst)
# 执行结果
# ['zhangsan', 'lisi', 'zhaoliu']
# ['zhangsan', 'lisi', 'wangwu']
# 发现原始的数据并没有被修改

def change_list2():
    del lst[2]
    lst.append("new value")
    print(lst)

change_list2()
print(lst)
# 执行结果
# ['zhangsan', 'lisi', 'new value']
# ['zhangsan', 'lisi', 'new value']
# 当我们执行删除的时候发现，数据发生了修改
# 这是因为一个列表占用的内存分为两个部分
# 第一部分：列表本上占用的内存地址
# 第二部分：列表中元素占用的内存地址
# 在change_list1()方法中的赋值，是将lst赋予了一个新的列表地址，等到方法执行完成，lst地址重新指向原来的列表地址，所以最后打印的还是原来列表的数据
# 在change_list2()方法中的删除和修改，是删除的列表中的元素，所以是真实的删除，而不是地址的引用



def change_list3():
    global lst
    lst = ["AA","BB","CC"]
    print(lst)

change_list3()
print(lst)
# 执行结果
# ['AA', 'BB', 'CC']
# ['AA', 'BB', 'CC']
# 在lst上面添加global ，修改列表的地址


