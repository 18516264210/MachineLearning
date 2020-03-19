


# all() 都为true才返回true，只要有一个为false，就返回false
# False,0 都表示false


a = all([False,0])
print(a)

b = all([False,1])
print(b)

c = all([1,2])
print(c)

# 0表示False
d = all([0])
print(d)

# 非0表示True
e=all([1])
print(e)
f=all([-1])
print(f)