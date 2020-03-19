import re

"""
找出一篇文章中出现次数最多的单词。大小写的暂时不考虑，只考虑完全匹配
"""
def top1():
    a = "Developers are constantly challenged with choose the most effective runtime, programming model,and architecture for their application's requirements and team's skill set. For example, some use cases are best handled by a technology stack based on synchronous blocking I/O architecture, whereas others would be better served by an asynchronous, nonblocking stack built on the reactive design principles described in the Reactive Streams Specification.Reactive Spring represents a platform-wide initiative to deliver reactive support at every level of the development stack: web, security, data, messaging, etc. Spring Framework 5 delivers on this vision by providing a new reactive web stack called Spring WebFlux, which is offered side by side with the traditional Spring MVC web stack. The choice is yours!"

    maxWord = ""
    maxTimes = 0

    # 将文章打散为单词数组。使用原生的字符串无法通过多个字符截断，所以这里使用外部包
    words = re.split('[.,]',a.replace(" ",","))
    wordsDict = {}
    for word in words:
        # 分割后的空串可能也会部分占用，去掉这部分数据
        if word == '' or word is None:
            continue
        # 从字典中获取指定的数据
        number = wordsDict.get(word)
        # print("word:%s,number:%s"%(word,number))
        # 如果获取到的数据为空，表示还未进行存储，将value设置为1
        if number == '' or number is None:
            wordsDict[word] = 1
        # 如果获取到的结果不为空，表示已经进行了存储，在该值基础上加1
        else:
            number = number + 1
            wordsDict[word] = number
            # 设置值的时候，同时比对当前最大值与刚更新值的大小，如果当前更新的值是最大的，则同时同步全局最大值为当前值
            if maxTimes < number:
                maxTimes = number
                maxWord = word

    print("maxWord:%s,maxTimes:%s"%(maxWord,maxTimes))
    print(wordsDict)

def main():
    top1()

if __name__ == "__main__":
    main()



