
# 占位符%s %d %f
# % 连接符

# name = input("name:")
# age = input("age:")
# phone = input("phone:")
# hometown = input("hometown:")
#
# info = """
#     ------------info of %s------------
#     name            %s
#     age             %s
#     phone           %s
#     hometown        %s
#     ---------------end----------------
#     """ % (name,name,age,phone,hometown)
#
# print(info)

name = input("name:")
age = input("age:")
info = """
        --------------------info of %s
        name %s
        age %s
        --------------------info of end
        """ % (name,name,age)
print(info)

