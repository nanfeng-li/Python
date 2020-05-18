
#多行注释   ctrl+/    '''/'''

#__name__ == "__main__"  调用时不执行


#__init__    initialize(初始化)  定义类时初始化
#__init__类似于构造函数，__del__类似于析构函数。也可以看到，由于python是动态语言，一旦对象没有引用，就会被析构。
class Person(object):
  def __init__(self):
      self.name = 'Jim'
      self.age = 23
if __name__ == '__main__':
   person = Person()
   print(person.name)
   print(person.age)

#多元（素）赋值
(x,y,z) = (3,4,5)    #x=3   y=4    z=5

'''     转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。'''
