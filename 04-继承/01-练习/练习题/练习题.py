#001.编写一个程序，找出所有能被7整除但不是5的倍数的数字，在2000和3200之间(包括两者)。得到的数字应该以逗号分隔的顺序打印在一行上。
#my answer
number =[]
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        number.append(i)

print(number)
# P001 solution
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
#编写一个程序，可以计算给定数字的阶乘。假设将以下输入提供给程序：8，然后，输出应为：40320
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

#对于给定的整数n，编写一个程序来生成一个字典，其中包含(i, i*i)一个在1和n之间的整数(都包含在内)。然后程序应该打印字典。
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
##编写一个程序，接受来自控制台的逗号分隔的数字序列，并生成一个包含每个数字的列表和元组。
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
