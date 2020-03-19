
# 读取  模特.txt文件的内容（文件是通过notepad++创建，设置的编码格式是GB2312）
# notepad++默认是通过UTF-8编码进行存的，故意设置为GB2312进行测试
# 由于设置的格式GB2312，所以文件在保存的时候是通过GB2312码表将具体的文件内容转化为二进制数据存储到硬盘
# 所以在读取这些二进制数据的时候，也需要通过GB2312码表进行转化，通过UTF-8去转化肯定会出现乱码或者转化不了的问题
# 由于GBK兼容GB2312所以这里使用GBK或者GB2312都可以使用


# f = open(file="F:/模特.txt",mode="r",encoding="UTF-8")
# f = open(file="F:/模特.txt",mode="r",encoding="GBK")
# mode=r表示读，通过文本的方式读，encoding指定读的时候使用的编码
f = open(file="F:/模特.txt",mode="r",encoding="GB2312")
data = f.read()
f.close()
print(data)


# 使用相对路径
ff = open(file="read.txt",mode="r",encoding="UTF-8")
ddata = ff.read()
ff.close()
print(ddata)