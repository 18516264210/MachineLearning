
# ASCII

# Erjinzhi 中讲述了如何将数字转化成二进制，然后计算机可以识别了数字

# 那么计算机是如何识别汉字，识别英文，识别俄文....的呢？？？？？？？

# 文字先转换为十进制，再由十进制转为二进制

# 那么文字是如何转换为十进制的呢？？？？？

# 有一张对应表ASCII，输入文字之后，按照对应表强转化为十进制(最大是255,8位)

# 计算机输入0123456789只是看到的数字，实际按照码表ASCII对应的是48,49,50,51,52,53,54,55,56,57
# 也就是说咱们看到的1实际上计算机认为他不是1，而是49

######################################################################################v

# 下面将部分的文字转化为二进制
# 将#tangjinyi转化为二进制，只举例子，具体对应的值可参照ASCII码表

#######################################################################
##    对应码表的值    128   64   32   16   8   4   2   1
## #      (51)         0    0    1    1    0   0   1   1
## t      (..)         0    0    1    1    0   0   1   1
## a      (..)         0    0    1    1    0   0   1   1
## n      (..)         0    0    1    1    0   0   1   1
## g      (..)         0    0    1    1    0   0   1   1
## j      (..)         0    0    1    1    0   0   1   1
## i      (..)         0    0    1    1    0   0   1   1
## n      (..)         0    0    1    1    0   0   1   1
## y      (..)         0    0    1    1    0   0   1   1
## i      (..)         0    0    1    1    0   0   1   1
#######################################################################

# 然后将二进制结果拼接到一起，前面的0可以去掉，中间没有空格
# #tangjinyi
# 那么计算机是如何分清楚拼接后的二进制是怎么对应字符串的呢？？
# 所以这里面一定要做好断句，不然计算机是识别不了的
# 前面已经讲过实际上所有的字符最大的ASCII码也就是255，也就是说最大的值也就是8位。
# 所以计算机将所有的字符都默认是8位，那么按照位数去读，每次都取8位置,这8位就代表一个字符。是不是可以分清了呢？答案是：是的

#######################################################################

# 每一位0或者1所占的空间单位为bit(比特)，这是计算机中最小的表示单位。注意：0或者1都占用空间
# 一个二进制位占用1bit

##################问题来了，前面介绍的ASCII码仅支持英文和符号，那么中文怎么办呢??########################
# 所以中文第一套编码表GB2312出现了，收录了常用的7445个图形字符,包括汉字6763个，且只支持简体
# 由于GB2312不完善，所以后来出现了GBK1.0，收录了21003个汉字，包括简体和繁体，兼容GB2312
# 后来又升级到GB18030，属于GBK的升级版，收录了27484个汉字，覆盖了少数民族语言，日本，韩国语

# 那么问题来了，如果每个国家都出一套编码，日本的软件安装到中国的windows系统上，显示的全是乱码，因为中国的电脑不会装日本的码表，所以转化是有问题的
# 那怎么办呢？我装日本软件的时候，还需要安装一个日本的码表

# 此时ISO国际标准组织出现了，需要出一个支持全世界的编码Unicode
# 规定所有的字符最少都由16位表示（2bytes）,这个表的大小为2**16=65536：
# 由于一个字符占用16位，把16位沾满表示是表中最大的数，所以说这个码表的大小为最大值
# 对于中国来说，这个正好，但是英国和美国不满意了，因为英文本来就不占用空间，现在都得占用16位


# 最后出现了UTF-8编码，对Unicode进行了优化，做成可变长的存储
# 英文使用1个字节存储，欧洲使用2个字节，中文使用3个字节























