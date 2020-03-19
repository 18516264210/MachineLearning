
# 50不打印
# 60-80之间的数打印平方

count = 0
while count <= 100:
    if count == 50:
        pass # 什么也不干
    elif count >= 60 and count <= 80:
        print(count*count)
    else:
        print(count)
    count += 1