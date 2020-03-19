"""
    使用选择排序法进行数据的排序
    什么是选择排序，通过内层循环，找到值最大的索引，然后将最大值放在最后面；
    或者是通过内层循环，找到值最小的索引，然后将最小值放在最前面。
    正序和逆序无所谓
"""

def select_sort_1():
    """对数组进行从小到大排序，先排小值到最前"""
    data = [9,3,7,6,5,4,8,2,1]
    for i in range(len(data)):
        index = i
        # 从index开始遍历，与下一个元素进行比较，获取到值为最大的index
        for j in range(i,len(data)):
            # 这里获取到的是值为最小的index，并且将当前位置i替换为本次循环的最小值。
            # 即：这里排序是先排小元素，再排大元素
            if data[index] > data[j]:
                index = j
        if not index == i:
            data[i], data[index] = data[index], data[i]

    return data

def select_sort_2():
    """对数组进行从小到大排序，先排大值到最后"""
    data = [9, 3, 7, 6, 5, 4, 8, 2, 1]
    for i in range(len(data)-1):
        index = 0
        # 这里找到最大的index
        for j in range(len(data)-i):
            if data[index] < data[j]:
                index = j
        #  将最大的元素放在最后面，所以这里需要通过下标，定位到最后
        if not index == i:
            data[len(data)-i],data[index] = data[index],data[len(data)-i]
    return data;

def main():
    print(select_sort_2())
    
    a = (1,2,3,4,5,6)
    print(a[0])


if __name__ == "__main__":
    main()