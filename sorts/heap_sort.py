
"""
手写堆排序，这里使用的是大顶堆
"""

def heap_sort():
    """对数组进行从小到大排序"""
    data =[65, 87, 12, 3, 94, 53, 44, 36, 27]
    dsort(data,len(data))
    return data

def dsort(data, heap_size):
    """如果heap_size=9，i=0,1,2,3"""
    size = heap_size // 2
    for i in range(size):
        index = size - 1 - i
        print("index:%s,size:%s"%(index,heap_size))
        heap_heapify(data, index, heap_size)

    size2 = heap_size
    for i in range(1,size2):
        index = size2 - i
        print("heapsize:%s,i:%s"%(heap_size,index))
        data[index], data[0] = data[0], data[index]
        heap_size = heap_size - 1
        heap_heapify(data, 0, heap_size)

def heap_heapify(data, root, heap_size):
    maximum = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2

    if left_child < heap_size and data[left_child] > data[root]:
        maximum = left_child
    if right_child < heap_size and data[right_child] > data[maximum]:
        maximum = right_child
    if root != maximum:
        data[root], data[maximum] = data[maximum], data[root]
        heap_heapify(data, maximum, heap_size)



def main():
    print(heap_sort())


if __name__ == "__main__":
    main()