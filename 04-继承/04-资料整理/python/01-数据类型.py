#字符串:就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号

name = 'hello world'
print(name.title())   #通过name.title()调用了字符串自身的一个函数title()，这个函数的作用就是将每个单词的首字母大写。
print(name.upper())     # 全部大写输出
print(name.lower())     # 全部小写输出

#Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip() 。
language = 'python  '
print(language)
print(language.rstrip())       # 删除空白
print(language)

language = language.rstrip()    #要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
print(language)
#还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip() 和strip() ：
fruit = ' apple'
print(fruit.lstrip())
fruit = ' banana '
print(fruit.strip())

#在Python中，可对整数执行加（+ ）减（- ）乘（* ）除（/ ）运算。（%）取余，（**）乘方
#使用函数str() 避免类型错误
age = 20
message = "Happy" + str(age) + "Birthday!"
print(message)

#列表:由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；
        # 也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
#用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
fruits = ['apple', 'banana', 'pear', 'watermelon', 'peach']
print(fruits)
print(fruits[0]) #返回第一个
print(fruits[-1])   #返回最后一个
#修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
fruits[0] = 'Kiwi fruit'
print(fruits)
#将元素附加到列表末尾。不影响列表中原来的元素。
fruits.append('durian')
print(fruits)
#方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
fruits.insert(0, 'durian')
print(fruits)
#知道要删除的元素在列表中的位置，可使用del语句。
del fruits[0]
print(fruits)
#方法pop()删除的是列表末尾的元素，并将该元素返回。
fruit = fruits.pop()
print(fruits)
print(fruit)
#可以使用pop()方法来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
fruit = fruits.pop(2)
print(fruits)
print(fruit)
#不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
# 假如，我要从列表中删除banana，我可以这样写：
fruits.remove('banana')
print(fruits)
#注意：方法remove()也会返回被删除的元素值，而且它只能删除第一个指定的值，也就是说，如果一个列表中存在多个你要删除的元素，
# 那么它只能删除第一个，剩下的相同元素将不能删除。所以，我们得通过循环来判断是否删除了所有这样的值。

#sort() 让你能够较为轻松地对列表进行排序,会永久性地改变列表的元素位置
fruits.sort()
print(fruits)
#可以按与字母顺序相反的顺序传递，要想实现，只需向sort()方法传递参数reverse=True。
fruits.sort(reverse=True)
print(fruits)
#要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted() 。

# 函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
print(sorted(fruits))
print(fruits)
#因为sorted()方法会返回一个新的列表，所以该方法是不会对原列表进行任何修改的。
# 如果你要按与字母相反的顺序排序，同样地传入reverse=True即可。

#倒着打印列表，可使用方法reverse()。
fruits.reverse()
print(fruits)
#注意：方法reverse()会永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，
# 要想实现，我们只需要再次调用reverse()方法即可。

#使用函数len()可以快速得到一个列表的长度。
print(len(fruits))

#使用for循环遍历列表
for fruit in fruits:
    print(fruit)
print('循环结束')
#这段程序让Python从列表中每次都取出一种水果，并将其储存到变量fruit中，然后打印fruit的值。

#使用range()函数创建数字列表：
for value in range(1, 5):
    print(value)
#将range()产生的数字直接转换为列表：
number = list(range(1, 6))
print(number)
#使用range()函数时，我们还可以指定步长。例如：我要想输出1~10内的偶数：
number = list(range(2, 11, 2))
print(number)
#创建一个列表，其中包含前10个整数的平方。
numbers = []
for value in range(1, 11):
    number = value ** 2
    numbers.append(number)
print(numbers)
#统计函数
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

#要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range() 一样，Python在到达你指定的第二个索引
# 前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0 、1 和2 的元素。
fruits = ['apple', 'banana', 'pear', 'watermelon', 'peach']
print(fruits[0:3])
#如果你没有指定第一个索引，Python将自动从列表开头开始：
print(fruits[:4])
print(fruits[2:])   #第三个元素到列表末尾的所有元素
print(fruits[-3:])  #输出列表中的最后三个元素
#如果要遍历列表的部分元素，可在for循环中使用切片，例如：我们遍历列表中的前三个元素。
for fruit in fruits[0:3]:
    print(fruit)
#复制切片,得到了一个新的列表fruits_new，两个列表的元素均相同。
fruits_new = fruits[:]
print(fruits)
print(fruits_new)
#赋值，新列表和原列表指向的是同一个列表
fruits_new = fruits
print(fruits_new)

#元组:看起来就像列表，但使用圆括号而不是方括号来标识,定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
number = (4, 6, 2, 1, 9, 7)
print(number[0])
#和列表一样，我们也可以通过for循环来遍历元组。
number = (4, 6, 2, 1, 9, 7)
for num in number:
    print(num)
#在Python中虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，要想改变元组的元素，我们可以重新给元组赋值。
number = (4, 6, 2, 1, 9, 7)
for num in number:
    print(num)
number = (1, 2, 3, 4, 5, 6)
for num in number:
    print(num)








