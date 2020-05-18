#函数input() 的工作原理
#函数input()能让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python会将其存储在一个变量中，例如下面的程序：
age = input('请输入你的年龄:')
print(age)
#使用int() 来获取数值输入
#当我们使用input()进行输入时，Python会将输入的内容解读为字符串：
age = input('请输入你的年龄:')
if age > 18:
    print(age)      #会报错
#当你试图对age进行数值操作时，程序就会报错，因为age变量存储的是字符串而不是数字。
age = input('请输入你的年龄:')
age = int(age)
if age > 18:
    print(age)
#输出1~100的偶数：
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
#while循环和for循环类似，但也有些许不同。
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
#选择何时退出
mess = ''
while mess != 'quit':
    mess = input('请输入:')
    print(mess)
#在用户输入之后，程序会进行检查，只有当用户输入的内容不为quit时才会进行输出。
mess = ''
while mess != 'quit':
    mess = input('请输入:')
    if mess != 'quit':
        print(mess)
#通过标记退出while循环
flag = True
HP = 10
while flag:
    message = input('请输入:')
    if message == 'quit':
        flag = False
    else:
        print(message)
    HP -= 1
    if HP == 0:
        flag = False
#要立即退出while循环，可使用break语句，break 语句用于控制程序流程，可使用它来控制哪些代码行将执行，
# 哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
while True:
    mess = input('请输入:')
    if mess == 'quit':
        break
    else:
        print(mess)
#要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，它不像break
# 语句那样不再执行余下的代码并退出整个循环。例如，来看一个从1数到10，但只打印其中偶数的循环：
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)
#上述程序段中，我们让其在对num求模不等于0时结束当前循环，重新回到循环开始。这样奇数就无法运行到输出语句了。

#使用while循环来处理列表和字典
#for 循环是一种遍历列表的有效方式，但在for 循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while 循环。通过将while 循环同列表和字典结合起来使用，可收集、
# 存储并组织大量输入，供以后查看和显示。
#在列表之间移动元素
fruits = ['apple', 'pear', 'banana', 'orange', 'Hami']
fruits_new = []

while fruits:
    fruit = fruits.pop()
    fruits_new.append(fruit)

print(fruits)
print(fruits_new)
#删除包含特定值的所有列表元素
fruits = ['apple', 'pear', 'banana', 'orange', 'Hami', 'pear', 'apple', 'pear']
while 'pear' in fruits:
    fruits.remove('pear')
print(fruits)
#使用用户输入来填充字典
#可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。
# 我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：
while flag:
    name = input('请输入姓名:')
    response = input('请输入您的爱好:')
    # 将信息存储到字典
    responses[name] = response

    repeat = input('是否还有人要参与调查(yes/no)')
    if repeat == 'no':
        flag = False
# 输出结果
print(responses)
