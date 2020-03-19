
# 写文件
# 情况，然后写入，不会是追加

# 默认编码是UTF-8，这里指定写的编码是GBK
# 这里的流程是：先将需要写的内容转为Unicode在内存 ，然后再将内存的数据通过GBK的格式写入到磁盘中
# 这里需要注意的是文件的格式是什么。如果UTF-8的文件写入GBK的内容也是会有问题的。不过这个问题只是显示的问题，可以调节文件的查看编码即可

ff = open(file="新文件1.txt",mode="w",encoding="GBK")
ff.write("我是通过python程序写入到文件的，我以￥作为标记，我的编码格式是GBK，你不要试图通过UTF-8来读取我的信息哦00000")
ff.close()
print("---------------------------------------------------------写入完毕")

# fff = open(file="read.txt",mode="r",encoding="UTF-8")
fff = open(file="新文件1.txt",mode="r",encoding="GBK")
data = fff.read()
print(data)
fff.close()


# 从远程接收到一些二进制的数据，通过UTF-8编码进行数据的存储
print("-------------------------------------------")
ffff = open(file="新文件2.txt",mode="wb")
# ffff.write("我是从外面传递过来的数据")
# 需要指定通过什么方式的编码进行存储
# TypeError: a bytes-like object is required, not 'str'

ffff.write("我是从外面传递过来的数据".encode("UTF-8"))
ffff.close()







