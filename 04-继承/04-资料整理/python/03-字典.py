#字典是一组特殊数据的集合，它通常用来描述一个事物的属性
#字典是一系列键——值对，每个键都有一个唯一的值与其对应，
# 你可以使用键来访问与之相关的值。这个值可以是数字、字符串、列表甚至字典。

#要想访问字典的值，我们可以通过其对应的键来访问：
person = {'name': 'zhangsan', 'age': 20}
print(person['name'])
print(person['age'])
#字典是一种动态结构，可随时在其中添加键值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
person = {'name': 'zhangsan', 'age': 20}
person['height'] = 180
person['weight'] = 110
print(person)
#要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
person = {'name': 'zhangsan', 'age': 20}
person['age'] = 22
print(person)
#对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。使用del 语句时，必须指定字典名和要删除的键。
person = {'name': 'zhangsan', 'age': 20}
del person['name']
print(person)

#遍历字典
person = {'name': 'zhangsan', 'age': 20, 'height': 180, 'weight': 110}
for key,value in person.items():
    print('key:' + key + '---value:' + str(value))
#通过item()函数获得字典的每个键值，然后定义两个变量key，value分别存储键和值。即可输出字典的所有值。
#注意：Python不关心键值对的存储顺序，所以在遍历字典的时候，顺序可能和原字典不同。
#遍历字典时，会默认遍历所有的键，如果显式地使用方法keys()可让代码更加容易理解，你可以选择这样做，也可以省略它
person = {'name': 'zhangsan', 'age': 20, 'height': 180, 'weight': 110}
for value in person.keys():
    print(person[value])
#方法keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键。
person = {'name': 'zhangsan', 'age': 20, 'height': 180, 'weight': 110}
keys = person.keys()
print(keys)

#使用函数sorted() 来获得按特定顺序排列的键列表的副本：
person = {'zhangsan': 20, 'lisi': 24, 'wangwu': 18, 'zhaoliu': 28}
for name in sorted(person.keys()):
    print(name)
#按顺序遍历字典中的值：
person = {'zhangsan': 20, 'lisi': 24, 'wangwu': 18, 'zhaoliu': 28}
for age in sorted(person.values()):
    print(age)
#使用集合(set)，对字典中的值进行去重操作
person = {'zhangsan': 20, 'lisi': 20, 'wangwu': 18, 'zhaoliu': 28}
for age in set(person.values()):
    print(age)

#使用字典和列表我们可以组合出复杂的数据。
person1 = {'name': 'zhangsan', 'age': 20}
person2 = {'name': 'lisi', 'age': 22}
person3 = {'name': 'wangwu', 'age': 21}
person = [person1, person2, person3]
print(person)
#在字典中存储列表
person = {
    'name': 'zhangsan',
    'age': 20,
    'hobby': ['篮球', '足球', '游泳']
}
print(person)
#在字典中存储字典
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
