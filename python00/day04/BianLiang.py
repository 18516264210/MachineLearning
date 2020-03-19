# coding:UTF-8

# 演示了python语言在方法传递参数中的不同方式。包括固定参数，非固定参数，默认参数，元组，列表等不同类型

print("-----------------------位置参数------------------------")
# 定义函数，设置两个参数name，age
# 传递参数的时候使用的是按照顺序进行的，所以就叫做位置参数
def register_function(name,age):
    print("my name is ",name,",I`m ",age," years old")

register_function("zhangsan",18)

print("-----------------------默认参数------------------------")

# 设定函数的默认参数，如果大多数的参数都是一致的，可以使用默认参数，在函数中定义默认参数，且设置默认值。
# 这样，在调用函数的时候就可以不用指定该参数的值，在执行的时候使用默认的值。
# 如果指定了参数的值，那么在执行的时候就使用指定的值。
# 如下面的country，默认是北京，如果指定了上海，那么就会将北京覆盖，使用上海作为真实的值。
# 注意：使用默认值的时候一定要放在方法的最后面。
def register_moren(name,age,country="北京"):
    print("my name is ",name,",I`m ",age," years old",",I`m from ",country)

register_moren("lisi",19)
register_moren("wangwu",20,"上海")

print("-----------------------关键参数------------------------")
# 方法中定义两种参数，一种位置参数：name，age，一种默认参数：country，school
# 在调用的时候，可以country="上海",age=22,school="ps" 这种key：value的方式进行调用，并且可以忽略函数参数定义的顺序
#重要: 但是如果位置参数被默认参数占用，那么位置参数一定要带上key，这种就是关键参数
def register_guanjian(name,age,country="北京",school="ps"):
    print("my name is ",name,",I`m ",age," years old",",I`m from ",country,",my primary school is ",school)

register_guanjian("张三",country="上海",age=22,school="ps")
# 这种方式是不行的
# register_guanjian("张三", country="上海", 22,school="ps")

print("-----------------------非固定参数1------------------------")
# 前面介绍的都是传递的int，或者str类型的参数。那么我如果需要传递类似于java中的list，或者map怎么办呢？？
# 给多个人发消息
# 在参数前面加*号，表示这个是一个元组，传递多个参数的时候，会被打包然后传递给users。
# 当然也可以先把元组打包好进行传递，此时就不需要前面的*号了
# 有点儿类似于java中的list
def register_feiguding(msg,*users):
    for u in users:
        print(u,"收到了消息:",msg)

register_feiguding("我是报警信号","zhangsan","lisi","wangwu")
print("-------------------------------feiguding---------------1---------------")
# 这种方式也可以，添加*会将作为一个参数打包成元组
# 这里一定要添加*号，否则该数组会作为一个整体
register_feiguding("我是报警信号",*["zhangsan","lisi","tianqi"])
print("-------------------------------feiguding---------------2---------------")

# 如果后面还添加参数的话，需要使用关键参数进行传递，否则函数无法判别是否是属于元组中的数据
def register_feigudingg(msg,*users,age):
    for u in users:
        print(u,"收到了消息:",msg)

# 这种方式可以使用，使用关键参数
register_feigudingg("我是报警信号","zhangsan","lisi","wangwu",age=22)

print("-------------------------------feiguding---------------3---------------")


print("-----------------------非固定参数2------------------------")
# 前面介绍了可以传递多个参数，通过*可以自动打包，那么我直接传递元组，结果会是怎么样的呢？
# 答案是肯定的，可以呀
users = ("zhangsan","lisi","zhaoliu");
def register_feiguding2(msg,users):
    for u in users:
        print(u,"收到了消息:",msg)

register_feiguding2("哈哈哈，我是消息",users)

print("-----------------------非固定参数3------------------------")
# 上面介绍了如何传递int，string，元组，那么如何传递多种复杂的数据类型呢？？
# 使用了**这种类型的参数后，发现其实这种方式更适合
# 元组类型的数据还需要遍历，且不知道如何获取到执行的值，而使用字典类型的数据，可以通过key直接得到数据的值
def register_feiguding4(name,*args,**kwargs):
    print(name,args,kwargs)

# 发现后面的aa，bb，cc都放在了args参数中，而kwargs中的数据为空
register_feiguding4("张三","aa","bb","cc")
# kwargs接收的是dict类型的数据，也就是keyvalue参数，或者说是关键参数
register_feiguding4("张三","aa","bb","cc",AA="AA",BB="BB",CC="CC")

# 参数篡位，使用下面的方式进行传递，会出现什么结果呢？
# 张三 ({'school': 'primary school'},) {}
# d会作为元组的一个元素，而后面的参数为空
# 如果在d前面添加**，那么就正常了，类似于全面提到的在参数前面加* 一样
# 张三 () {'school': 'primary school'}
d = {"school":"primary school"}
register_feiguding4("张三",d)
register_feiguding4("张三",**d)


print("-----------------------非固定参数4------------------------")

def register_feiguding5(args):
    print(args)

ar={"school":"primary school","name":"lixiaosi"}
register_feiguding5(ar)

print("-----------------------非固定参数5------------------------")

# 为什么这里直接传递列表就可以呢
def register_feiguding6(users):
    for u in users:
        print(u)

users={"a","b","c","d"}
register_feiguding6(users)

print("-----------------------非固定参数6------------------------")
# 传递字典类型的数据
def register_feiguding7(users):
    for key in users:
        print(key,"对应的value为",users[key])
    #能否直接获取数据呢？答案是可以的
    print(users["sex"])

boy={"name":"liuxiaosheng","sex":"男","age":39}
register_feiguding7(boy)