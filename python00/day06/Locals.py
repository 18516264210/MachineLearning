

x = 1
y = "zhangsan"

# locals()，函数内的名称空间，包括局部变量和形参。当前所在的
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000004760B8>,
#  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'F:/IdeaProjects/python37/python00/day06/Locals.py',
# '__cached__': None, 'x': 1, 'y': 'zhangsan'}
print(locals())

# globals()，全局变量，函数定义所在模块的名称空间
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000004760B8>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'F:/IdeaProjects/python37/python00/day06/Locals.py',
#  '__cached__': None, 'x': 1, 'y': 'zhangsan'}
print(globals())

# 内置模块的名字空间
print(__builtins__)
# dir(__builtins__)

