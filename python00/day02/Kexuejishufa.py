
from decimal import *
# 科学计数法
# 表示13999
# 1.3999*10~4，使用python的表示是1.3999e4
s = 1.3999e4
print(s)

# 复数，这里是j，不是i
# 4是实部,5是虚部
f = (4+5j)
print(f)


print("----------------------------------------------------------")
# 浮点数的精度
# 浮点数所占的空间远大于整数
# python默认的是17位的精度，也就是说小数点后16位，越到后面越不精确
# 打印的结果是：12.578283828823848，后面的自动四舍五入
ff = 12.578283828823848938486248327472636
print(ff)

# 如果需要使用精度更高的数字，那么怎么办呢？
# 引入decimal，通过设置getcontext().prec的值来设定精度
print(getcontext())
getcontext().prec = 50
m = Decimal(1)/Decimal(3)
print(m)
getcontext().prec = 10
m = Decimal(1)/Decimal(3)
print(m)






