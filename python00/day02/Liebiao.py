
# 列表
# 列表可以存放任意类型的数据

# 创建
print("--------------------列表的创建-----------------------")
L1 = []
L2 = ["a","ab","c",2,"c"]
L3 = ["a",["ab","c"],2]
print("创建空列表：",L1)
print("列表的值是可以重复的：",L2)
print("创建复杂列表：",L3)

L4 = list()
print("通过list()创建列表：",L4)


print("--------------------列表的查询-----------------------")
v = L2[2] #这里的2是索引,索引从0开始
print("通过索引查询：",v)
v = L2[-1]
print("从最右边开始取值:",v)
v = L2[-2]
print("获取倒数第二个值:",v)
v = L2[-3]
print("获取倒数第三个值:",v)
index = L2.index("c")
print("根据实际值c获取第一个索引值(从左往右)：",index)
# index = L2.index("ddd")
# print("未找到索引值，会报错：",index)
c = L2.count("c")
print("统计L2中c的个数:",c)


print("--------------------列表的切片，后面的为开区间，前面的为闭区间-----------------------")
cp = L2[0:3]
print("获取L2的前三个数据L2[0:3]，注意使用冒号：",cp)
cp = L2[1:3]
print("获取L2的中间的数据L2[1:3]，注意使用冒号：",cp)
cp = L2[0:-1]
print("0到最后一个，不包括最后一个L2[0:-1]，注意使用冒号：",cp)
cp = L2[-3:-1]
print("获取L2后面的数据，发现后面的数据丢了L2[-3:-1]，注意使用冒号：",cp)
cp = L2[-3:0]
print("获取L2后面的数据，发现使用0也不行L2[-3:0]，注意使用冒号：",cp)
cp = L2[-3:]
print("获取L2后面的数据，后面的不写可以L2[-3:]，注意使用冒号：",cp)
cp = L2[:3]
print("前面的部分不写呢L2[:3]，注意使用冒号：",cp)
cp = L2[:]
print("前面后面都不写呢L2[:]，注意使用冒号：",cp)

cp = L2[::2]
print("2是步长L2[::2]，注意使用冒号：",cp)

print("--------------------列表的增加-----------------------")
libiao = ["zhangsan","lisi","wangwu","1","2","2",["3",4,"zhaoliu"],"tianqi","sunba"]
# 在最后面追加
libiao.append("qianjiu")
print("追加一个qianjiu:",libiao)
# 1表示索引所在的位置
libiao.insert(1,"xiaolisi")
print("在index为1的位置添加xiaolisi:",libiao)

print("--------------------列表的修改-----------------------")
# 直接通过索引赋值修改数据
libiao[1] = "dalisi"
print("将index为1的值改成dalisi",libiao)

print("--------------------列表的删除-----------------------")
# 通过pop删除
libiao.pop()
print("通过pop删除最后一个元素：",libiao)
libiao.remove("lisi")
print("通过remove删除lisi：",libiao)
libiao.remove("2")
print("通过remove删除有重复的元素2，发现值删掉了左起第一个：",libiao)
del libiao[1]
print("使用del删除指定索引或者指定索引范围内的元素:",libiao)

print("--------------------列表的复制-----------------------")
list1 = ["zhangsan","lisi","wangwu","zhaoliu"]
# 列表和值是独立的。也就是说列表会占用一定的空间，列表的值会占用独立的空间
# list2指向的是list1的位置，而不是list1值的位置，所以list1发生变更list2获取的值也会跟着变更
# 这里类似于java中的值传递和引用传递
list2 = list1
print("list1:",list1)
print("将list1赋值给list2:",list2)
list1[0] = "xiaozhangsan"
print("修改list1的zhangsan为xiaozhangsan:",list1)
print("list2的zhangsan也改变成了xiaozhangsan:",list2)

print("--------------------列表的浅拷贝-----------------------")
list3 = list1.copy()
print("list1:",list1)
print("将list1复制给list3，这里只是复制了一个列表的地址，而没有将内部的值复制:",list3)
list1[1] = "xiaolisi"
print("list1的lisi改成xiaolisi:",list1)
print("list2的lisi也改成了xiaolisi:",list2)
print("list3的list还是lisi:",list3)

print("--------------------id()查看内存地址-----------------------")
# id()查看内存地址
print("查看列表的内存地址list1：",id(list1))
print("查看列表的内存地址list2：",id(list2))
print("查看列表的内存地址list3：",id(list3))