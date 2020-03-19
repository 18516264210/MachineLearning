# ReadFile12介绍了通过rb的模式读取二进制文件
# 最终人是无法识别的
# 我们把问题交给了别人，让别人来处理?
# 那么问题来了：假如哪个接收二进制文件的人是我自己怎么办呢？？？？
# 可以借助第三方工具包chardet，使用detect方法进行检测
# 这个需要安装 pip install chardet

import chardet


ff = open(file="F:/模特.txt",mode="rb")
data = ff.read();

# 打印结果显示99%的可能是GB2312
# {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
print(chardet.detect(data))
print("-------------------根据检测结果进行解码-------------------")
result = data.decode("GB2312")
print(result)
ff.close()