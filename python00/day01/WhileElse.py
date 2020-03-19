
# 循环执行完成会执行else，也就是说不符合while的条件了

# count = 0
# while count < 6:
#     print("loop",count)
#     count += 1
# else:
#     print("循环执行完成")
#
# print("------------the end-----------")


# 跳出循环是不会执行else语句的
count = 0
while count < 6:
    if count == 4:
        break

    count += 1
    print("loop",count)
else:
    print("循环执行完成")

print("------------the end-----------")