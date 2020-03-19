import math
"""
手写堆排序，这里使用的是大顶堆
"""

def heap_sort(data, size):
    """对数组进行从小到大排序"""

    # 构建大顶堆
    build_max_heap(data, size)
    for i in range(size-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        size = size - 1
        heapify(data, 0, size)

def build_max_heap(data, size):
    """
     第一次进入，root=3，left=7，right=8，比较后largest=7，递归后发现都下标越界，递归结束，进入到for
        此时数据为[65, 87, 12, 36, 94, 53, 44, 3, 27]
     第二次进入，root=2，left=5，right=6，比较后largest=5，递归后发现都下标越界，递归结束，进入到for
        此时数据为[65, 87, 53, 36, 94, 12, 44, 3, 27]
     第三次进入，root=1，left=3，right=4，比较后largest=4，递归后发现无法进行再次递归，递归结束，进入到for
        此时数据为[65, 94, 53, 36, 87, 12, 44, 3, 27]
     第四次进入，root=0，left=1，right=2，比较后largest=1，进入到递归
        此时数据为[94, 65, 53, 36, 87, 12, 44, 3, 27]
     第五次进入，root=1，left=3，right=4，比较后largest=4
        此时数据为[94, 87, 53, 36, 65, 12, 44, 3, 27]
     到此，大顶堆就已经构建完毕了
     TODO 为什么从3,2,1,0开始，为什么构建大顶堆是这样构造的，跟数组有什么关系？
     说明：将数组的数据前向后构建完全二叉树【堆结构是一个完全二叉树】，如下图所示。
                     65
                  /   |
                87    12
              / |    / |
            3 94  53 44
          / |
        36 27
    遍历开始是3,2,1,0，是因为这些节点不是叶子节点，也就是说找到非叶子节点，开始交换数据构建大顶堆
    变换完成后，数组的数据是[94, 87, 53, 36, 65, 12, 44, 3, 27]，对应的堆结构如下所示，已经是一个大顶堆
                     94
                  /   |
                87    53
              / |    / |
            36 65  12 44
          / |
        3 27
    """
    for i in range(len(data)//2-1, -1, -1):
        heapify(data, i, size)


def heapify(data, root, size):

    left = 2 * root + 1
    right = 2 * root + 2
    largest = root
    if left < size and data[left] > data[largest]:
        largest = left
    if right < size and data[right] > data[largest]:
        largest = right
    if largest != root:
        data[root], data[largest] = data[largest], data[root]
        print(data)
        heapify(data, largest, size)

def main():
    data = [65, 87, 12, 3, 94, 53, 44, 36, 27]
    heap_sort(data, len(data))
    print(data)


if __name__ == "__main__":
    main()