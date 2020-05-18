#列表元素转换为字符串：
a=['hello']
b=''.join(a)
print(b)

a=['hello','python']
b=''.join(a[1])
print(b)

#列表元素转换为元组：
def str2tuple(*str):
    return str

a=['hello', 'python']
b=str2tuple(a[0], a[1])
print(b)

#元组转换为字符串：
a=('hello', 'python')
b= ''.join(a[0])
print(b)

#元组元素转换列表：
a=('hello', 'python')
b=list(a)
c=list(a[0])
print(b)
print(c)

#字符串转换为元组：
def str2tuple(*str):
    return str
a='hello world!'
b=tuple(a)
c=str2tuple('hello world!')
print(b)
print(c)

#字符串转换为列表：
def str2tuple(*str):
    return str
a='hello world!'
b=list(a)
c=str2tuple(a)
e=list(str2tuple(a))
print(b)
print(c)
print(e)


# s = "xxxxx"
# list(s)
# ['x', 'x', 'x', 'x', 'x']
# tuple(s)
# ('x', 'x', 'x', 'x', 'x')
# tuple(list(s))
# ('x', 'x', 'x', 'x', 'x')
# list(tuple(s))
# ['x', 'x', 'x', 'x', 'x']

# 列表和元组转换为字符串则必须依靠join函数
#  "".join(tuple(s))
# 'xxxxx'
# "".join(list(s))
# 'xxxxx'
# str(tuple(s))
# "('x', 'x', 'x', 'x', 'x')"