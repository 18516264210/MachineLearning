
"""
    使用归并排序法进行数据的排序。
    归并排序分两步，第一步先对原始数组进行拆分，然后再对分散的数据进行组合。
    这里的分拆需要进行递归操作
"""

def merge_sort(data, start, end):
    """对数组进行从小到大排序。"""

    if end > start:
        middle = (start + end) // 2
        # 左半部分集合进行排序
        merge_sort(data, start, middle)
        # 右半部分集合进行排序
        merge_sort(data, middle+1, end)
        # 将左右子集合合并，即完成整个集合的排序
        do_merge(data, start, middle, end)

def do_merge(data, start, middle, end):
    # 创建临时数组，存放已经排序的数据
    sort_arr = [0 for i in range(len(data))]

    # 声明index_1、index_2分别指向两个集合的首元素位置
    # 声明temp_arr_index指向临时集合的首元素位置
    index_1, index_2, temp_arr_index = start, middle+1, 0

    # 比较两集合元素，选择较小的元素添加到临时集合中
    while index_1 <= middle and index_2 <= end:
        if data[index_1] <= data[index_2]:
            sort_arr[temp_arr_index] = data[index_1]
            index_1 = index_1 + 1
        else:
            sort_arr[temp_arr_index] = data[index_2]
            index_2 = index_2 + 1
        temp_arr_index = temp_arr_index + 1

    # 集合1元素并未全部添加到临时集合，则添加剩余元素到临时集合中
    while index_1 <= middle:
        sort_arr[temp_arr_index] = data[index_1]
        index_1 = index_1 + 1
        temp_arr_index = temp_arr_index + 1

    # 集合2元素并未全部添加到临时集合，则添加剩余元素到临时集合中
    while index_2 <= end:
        sort_arr[temp_arr_index] = data[index_2]
        index_2 = index_2 + 1
        temp_arr_index = temp_arr_index + 1

    # 将数据重新写入到源数组中
    for i in range(temp_arr_index):
        data[start+i] = sort_arr[i]


def main():
    data = [9, 3, 7, 6, 5, 4, 8, 2, 1, 23, 45, 0, 11, 9, 6]
    merge_sort(data, 0, len(data)-1)
    print(data)


if __name__ == "__main__":
    main()