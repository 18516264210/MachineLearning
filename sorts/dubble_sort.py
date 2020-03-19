
"""使用冒泡排序法进行数据的排序"""

def dubble_sort():
    """对数组进行从小到大排序"""
    data =[9,3,7,6,5,4,8,2,1]
    for i in range(1,len(data)):
        # 从第一个元素开始遍历，与下一个元素进行比较，并互换位置。
        # 第一次将最大的值放在最后的位置。下一次排序就不需要再对最后一个元素排序了。
        for j in range(len(data)-i):
            if data[j] > data[j+1]:
                data[j+1],data[j] = data[j],data[j+1]
    return data


def main():
    print(dubble_sort())


if __name__ == "__main__":
    main()