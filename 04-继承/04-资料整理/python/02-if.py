fruits = ['apple', 'banana', 'pear', 'watermelon', 'peach']
for fruit in fruits:
    if fruit == 'apple':
        print(fruit.upper())
    else:
        print(fruit.title())

#检查特定值是否包含在列表中
print('apple' in fruits)
print('Hami' in fruits)
print('Hami' not in fruits)

#使用if语句处理列表
numbers = []
if numbers:
    for num in numbers:
        print(num)
else:
    print('列表为空')

