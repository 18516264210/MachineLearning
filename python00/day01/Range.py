
#从0开始
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
for i in range(0, 10):
    a.append(i)

print(a)


print("----------------------------1")

# 从1开始
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
for i in range(1, 10):
    b.append(i)

print(b)

print("----------------------------2")

# 步长为5
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
c = []
for i in range(0, 50, 5):
    c.append(i)

print(c)

print("----------------------------3")

# 负数
# [0, -2, -4, -6, -8]
d = []
for i in range(0, -10, -2):
    d.append(i)

print(d)

print("----------------------------4")

# 字典需要设置key:value
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
f = {}
for i in range(0,10):
    f[i] = i

print(f)


print("----------------------------5")

g = list(range(10))
print(g)

h = list(range(0,10))
print(h)

print("----------------------------6")

# 生成表达式
# 循环多次，并将第一个值作为循环下标的值，但是这里写死的是100，所以该数组的所有的值都是100
ii = [i for i in range(10)]
iii = [100 for i in range(10)]
iiii = [i for i in range(10) if i%2 == 0]
print(ii)
print(iii)
print(iiii)
