class a:     # 说明父类的私有成员无法在子类中继承
    def __init__(self):
        self.ge = 123
        self.__gene = 456

class b(a):
    def __init__(self, name):
        self.name = name
        self.__age = 18
        super(b, self).__init__()     # 这一行会报错
    
    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
        # print(self.__gene)       # 这一行也会报错

obj = b('xiaoming')
print(obj.name)
print(obj.ge)
# print(obj.__gene)   # 这里会报错
obj.show()
