
# 猜年纪

count = 0
age= 18

while count < 3:
    user_guess = int(input("age:"))
    if user_guess == age:
        print("猜对了")
        break
    elif user_guess > age:
        print("往小猜")
    else:
        print("往大猜")

    count += 1

    if count == 3:
        choice = int(input("是否还想继续玩？0继续，1停止:"))
        if choice == 0:
            count = 0
        else:
            break

print("---------the end--------")