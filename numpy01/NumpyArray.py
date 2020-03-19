
import numpy as  np

narr1 = np.array([1,2,3,4,5])
print(narr1)
print("=========================================1")

narr2 = [1,2,3,4,5]
print(narr2)
print("=========================================2")

narr3 = {1,2,3,4,5}
print(narr3)
print("=========================================3")

narr4 = np.array(range(5))
print(narr4)
print("=========================================4")

# 这里的效果跟上面的效果是一样的
narr5 = np.arange(5)
print(narr5)
print(narr5.shape)
print("=========================================5")

# 多维数组
narr6 = np.array([[4, 5], [6, 1]])
print(narr6)
print(narr6.shape)
print("=========================================6")