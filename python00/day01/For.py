

# for循环

#range(1,20)返回的是一个对象，而不是一个数组
d = {}
for i in range(10):
    d[i] = i+1
print(d)

print("============================")

# 这里只打印1-9，而不是1-10
for i in range(1,10):
    print(i)


print("================================================================")

for i in range(10):
    print(i)

print("===切割===")

for i in range(1,10):
    print(i)
