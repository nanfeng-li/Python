#定义函数
def showText():
    print('Hello!')
showText()
#向函数传递信息(括号内可以传递该函数所需的参数)
def showText(name):
    print('Hello!' + name)
showText('Jack')
#函数括号内的name即是形参，而在调用该函数时传入的‘Jack’即是实参。
#传递实参
#位置实参要求实参的顺序与形参的顺序相同。也就是说，形参的参数位置是怎样的，你再传递实参的时候，
# 参数位置也就应该是这样，因为在位置实参中，实参和形参是一一对应的。
def showText(name, age):
    print(str(name) + '今年' + str(age) + "岁了")
showText('Jack', 20)
#第二种传递实参的方式就是关键字实参。它要传递给函数的名称——值对，直接在实参中将名称和值进行一一对应，
# 因此以这种方式传递实参就不会混淆，关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
def showText(name, age):
    print(str(name) + '今年' + str(age) + "岁了")
showText(age=20, name='Jack')
#编写函数时，可以给每个形参指定默认值，这样当你在调用函数的时候，如果没有传递实参，Python将会使用形参中的默认值进行处理。
def showText(name, age=20):
    print(str(name) + '今年' + str(age) + "岁了")
showText('Jack')
#函数并非总是直接输出，相反，它可以处理一些数据，并返回一个或一组值。
# 函数返回的值被称为返回值，在函数中，可以使用return语句将值返回到调用函数的代码行。
def dealName(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

name = dealName('jimi', 'hendrix')
print(name)
#注意：我们需将形参middle_name移到参数末尾。
def dealName(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

name = dealName('john', 'hooker', 'lee')
print(name)
#函数可返回任何类型的值，包括列表和字典等复杂的数据类型。
def create_person(name, age):
    person = {'name': name, 'age': age}
    return person

person = create_person('张三', 20)
print(person)
#可将函数同之前的任何Python结构结合起来使用
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 这是一个无限循环!
while True:
    print("\n请输入你的名字:")
    f_name = input("姓: ")
    l_name = input("名: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
#将列表传递给函数后，函数就能直接访问其内容。

def greet_users(users):
    for name in users:
        print('Hello!' + name.title())

users = ['张三', '李四', '王五']
greet_users(users)
#将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何操作都是永久性的。
def deal_list(fruits):
    fruits.pop()

fruits = ['apple', 'banana', 'pear', 'orange']
deal_list(fruits)
print(fruits)
#有时候，需要禁止函数修改列表，这个时候，我们可以将列表的副本进行传递而不是传递原列表。
def deal_list(fruits):
    fruits.pop()
    return fruits

fruits = ['apple', 'banana', 'pear', 'orange']
fruits_new = deal_list(fruits[:])
print(fruits)
print(fruits_new)
#有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
#将函数的形参定义为*hobby，星号让Python创建了一个名为hobby的空元组，并将接收到的值都封装到这个元组中。
def deal_hobby(*hobby):
    print(hobby)

deal_hobby('足球', '篮球', '羽毛球', '乒乓球')
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def deal_hobby(name, *hobby):
    print(name + '的爱好:' + str(hobby))

deal_hobby('张三', '足球', '篮球', '乒乓球')
#上述程序段中，第一个实参张三会去匹配形参name，其余的三个实参都将存入形参hobby中。
#使用任意数量的关键字实参
def deal_hobby(name, **hobby):
    print(name + '的爱好:' + str(hobby))

deal_hobby(name='张三', ball='篮球', sport=' 跑步')

#要让函数是可导入的，得先创建模块。模块 是扩展名为.py的文件，包含要导入到程序中的代码。
#先创建demo9.py文件。
def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
#再创建demo10.py，通过import导入demo9模块。
import demo9;

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = demo9.sum(numbers)
print(sum)
#导入模块中的特定函数
from demo9 import sum

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = sum(numbers)
print(sum)
#在sum后面还可以跟上任意数量的函数名，中间用逗号分隔。
#若使用这种语法，调用函数时就无需使用句点。由于我们在import 语句中显式地导入了函数sum() ，因此调用它时只需指定其名称
#使用as给函数指定别名
from demo9 import sum as s;

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = s(numbers)
print(sum)
#使用as给模块指定别名
import demo9 as d

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = d.sum(numbers)
print(sum)

#导入模块中的所有函数
from demo9 import *

print(sum((1, 2, 3, 4, 5)))
