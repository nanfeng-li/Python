#python中类的创建，父子类的继承
class Ppoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print(class_name, "destroyed")


class Spring_Point(Ppoint):
    def __init__(self):
        Ppoint.__init__(self, 1, 2)
        # super(Spring_Point, self).__init__(1, 2)


if __name__ == "__main__":
    xx = Spring_Point()
    print(xx.__dict__)
    #以上是用old的方式来创建一个class， Ppoint, class Spring_Point继承Spring_Point， 在调用父类的构造函数的时候，必须使用
    #Ppoint.__init__(self, 1, 2)

    #新方式创建类
class Ppoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __del__(self):
    #    class_name = self.__class__.__name__
    #    print class_name, "destroyed"


class Spring_Point(Ppoint):
    def __init__(self):
        Ppoint.__init__(self, 1, 2)
        # super(Spring_Point, self).__init__(1, 2)


if __name__ == "__main__":
    xx = Spring_Point()
    print(xx.__dict__)
