

# 前面ReadFile1,ReadFile2,ReadFile3介绍了读文件，都是一次性的将文件读取到内存中
# 那么文件非常大怎么办呢，不可能一次性的将所有的文件读到内存中
# 一行一行读

ff = open("read.txt","r",encoding="UTF-8")
print(ff)

print("===============================================================")
for line in ff:
    print(line)

ff.close()


# 二进制的形式读取文件

fff = open("read.txt","rb")
print(fff)
for line in fff:
    print(line)

fff.close()