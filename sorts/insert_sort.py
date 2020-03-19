
"""使用插入排序法进行数据的排序"""

def insert_sort():
    """
    对数组进行从小到大排序。首先遍历元数组，然后进行前面的插入，在插入的时候将小的插入到前面，所以这个时候插入时候的遍历是从索引的前面
    进行遍历
    """

    data =[ 9, 3, 7, 6, 5, 4, 8, 2, 1]

    # i=3，前面的数据是3、7、9对应的索引分别是0、1、2
    for i in range(1, len(data)):
        # 当前指针
        x = data[i]
        # 获取当前指针对应的数据，与前面的数据进行大小排序，前面的数据已经做了大小排序，所以只需要从后往前遍历即可
        # 此时i=3，j=3，与data[2]、data[1]、data[0]进行比较
        for j in range(i, 0, -1):
            # j为当前位置，试探j-1位置
            if x < data[j-1]:
                data[j],data[j-1] = data[j-1],x
            else:
                break
    return data


def main():
    print(insert_sort())


if __name__ == "__main__":
    main()