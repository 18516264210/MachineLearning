import collections
import re
import sys
import time

"""
找出一个超大文件中出现频率最高的100个词
这里使用分治的方式先将大文件拆分为多个小文件，比如这里将大文件拆分为100个小文件。
需要思考的问题是每个小文件，需要选择前多少位的数据作为下次排序的数据呢？

"""

def split2():
    # 这里仅限于读取小文件，如果遇到大文件，必死无疑
    fileContent = open("E:/a/english.txt","r",encoding="UTF-8").read()
    spliter = re.compile("\n",re.S)
    manyFiles = spliter.split(fileContent)
    # 创建一个写文件的句柄
    fileWriter = open('E:/a/0.txt', 'a', encoding='utf8');
    # 遍历切片后的文本列表
    for i in range(len(manyFiles)-1):
        # 先将列表中第一个元素写入文件中
        fileWriter.write(manyFiles[i]);
        # 关闭当前句柄
        fileWriter.close();
        # 重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
        fileWriter = open('E:/a/' + str(i+1)+'.txt', 'a',encoding='utf8');

    # 关闭最后创建的那个写文件句柄
    fileWriter.close();

    print('split finished');

def split3():
    """
    读取大文件的正确姿态
    """
    fileWriter = open('E:/a/0.txt', 'wb');
    with open("E:/win7-64-zjb-2018.rar", "rb") as f:
        i = 0
        while True:
            i = i+1
            if i > 100:
                break

            buff = f.read(1024*1024)
            sizer = sys.getsizeof(buff)
            print("本次读取的数据大小：%s"%(sizer/1024))
            if buff:
                # 先将列表中第一个元素写入文件中
                fileWriter.write(buff);
                # 关闭当前句柄
                fileWriter.close();
                # 重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
                fileWriter = open('E:/a/' + str(i) + '.txt', 'wb');
            else:
                break

    print('split finished');


def split4():
    """
    如果是文本文件，可以使用逐行读取。
    但是逐行读取的速度是比较慢的。所以内存不是特别小的情况下，可以使用批量读取。速度要快N倍
    """

    with open("E:/a/english.txt", "r", encoding="UTF-8") as f:
        i = 0
        file_writer = open('E:/a/0.txt', 'a', encoding="UTF-8");
        while True:
            # buff = f.readline()
            buff = f.read(1024)
            if buff:
                if i < 100:
                    # 先将列表中第一个元素写入文件中
                    file_writer.write(buff);
                    # 关闭当前句柄
                    file_writer.close();
                    # 重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
                    file_writer = open('E:/a/' + str(i) + '.txt', 'a', encoding="UTF-8");
                    i=i+1
                else:
                    i = 0
            else:
                break


def top100(data,i):
    if i == 100:
        return
    with open("E:/a/"+str(i)+".txt", "r", encoding="UTF-8") as f:
        words_dict = {}
        while True:
            buff = f.read(1024 * 1024)
            if buff:
                words = re.split('[.,]', buff.replace(" ", ","))
                for word in words:
                    if word == '' or word is None:
                        continue
                    number = words_dict.get(word)
                    if number == '' or number is None:
                        words_dict[word] = 1
                    else:
                        number = number + 1
                        words_dict[word] = number
            else:
                break

        # 对words_dict进行排序，选择前100频率最高的单词。这里的排序是python3提供的。lambda输入x，输出value
        # 这里返回的是一个tupe集合，而不是字典集合，所以需要注意。
        sorted_list = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)
        index = 0
        for item in sorted_list:
            if index == 100:
                break
            data.append(item)
            index = index+1

    top100(data,i+1)

def merge(data):
    """data是元组集合，所以需要将再次进行合并"""
    sorted_words_dict ={}
    # 这里返回的是一个元祖，key为单词，value为单词在各文件出现的次数
    for item in data:
        value = sorted_words_dict.get(item[0])
        if value == '' or value is None:
            sorted_words_dict[item[0]] = 0
        else:
            value = value + item[1]
            sorted_words_dict[item[0]] = value

    sorted_words_list = sorted(sorted_words_dict.items(),key=lambda x:x[1],reverse=True)
    print(sorted_words_list)


def main():
    print("切分开始时间:%s" % (time.time()))
    split4()
    print("切分结束时间:%s" % (time.time()))

    print("排序开始时间:%s" % (time.time()))
    data = []
    top100(data,0)
    print("排序结束时间:%s" % (time.time()))

    print("合并开始时间:%s" % (time.time()))
    merge(data)
    print("合并结束时间:%s" % (time.time()))


if __name__ == "__main__":
    main()



