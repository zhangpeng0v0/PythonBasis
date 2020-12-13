# 关键字 is 和 == 的区别
# is 判断是否是同一个ID， == 判断内容是否一致


# 深拷贝和浅拷贝
import copy

a = [1, 2, 3, 4,]
b = a    # 浅拷贝 ， a, b同时指向一个ID ，当其中一个修改时，另外一个也会被修改
c = copy.deepcopy(a)   # 深拷贝，c单独开辟一个id，用来存储和a一样的内容
d = a[:] # 这样也是深拷贝
e = copy.copy(a)   # 当拷贝内容是可变类型时，那么就会进行深拷贝，如果是不可变类型时，那么就会进行浅拷贝
# 注意：深拷贝值得是复制内容。单独开辟一个内存，浅拷贝值得是两个变量同时指向一个内存ID。


# 私有化和Property
class Test(object):
        def __init__(self):
                self.__num = 100
        @getNum.setter   # 等同步于 property( setNum, getNum)
        def setNum(self, num):   # 将self.__num的属性封装
                self.__num = num
        @property  # 等同于 getNum = property(getNum)  默认的是getter方法
        def getNum(self):  # 获取__num的值
                return self.__num
        num = property(getNum, setNum)  # 使用关键字property 将getNum和setNum方法打包使用，并将引用赋予属性num
t = Test()
print(t.__num)  # 将会出错，表示输出私有属性，外部无法访问
t.__num = 200   # 这里将会理解为添加属性 __num = 200 ,而不是重新赋值私有属性
print(t.__num)  #  这里输出的200是定义属性__num，而不是self.__num
t.setNum(200)  # 通过set方法将私有属性重新赋值
t.getNum()  # 通过get方法获取__num的值
print(_Test__num)  # 私有属性其实是系统再私有属性前加上了一个_Test，就是一个下划线加类名
t.num = 300  # 调用类属性num，并重新赋值， prooerty会自动检测set方法和get方法，并将引用赋值给set方法
print(t.num)  # 输出类属性，并会自己检测使用get方法进行输出
# 注意：num前后没有下划线的是公有方法，_num前边有一个下划线的为私有方法或属性，子类无法继承，前边有两个下划线的
#一般是为了避免于子类属性或方法名冲突，无法在外部直接访问。前后都有双下划线的为系统方法或属性。后边单个下划线的可以
#避免与系统关键词冲突。


# 列表生成式
range(1, 100, 5)  # 第一个参数表示开始位，第二个参数表示结束位(不含)，第三个参数表示步长
a = [i for i in range(1, 10)]   # 列表生成式表示返回i的值，每次返回9次，每次返回i的值
a = [2 for i in range(1, 10)]  # 这里会返回2，并且返回9次
a = [i for i in range(10) if i%2==0 ]  # 表示在生成式内部加入if判断，当 i 除以 2 的余数等于0的时候将数值返回
a = [(i , j) for i in range(5) for j in range(5)]   # 表示将 i 和 j 的值以元祖为元素的形式返回，当 i 循环一次的时候 j 循环5次


# 生成器
a = (i for i in range(1, 10))  # 将列表生成式外部中括号改为小括号，就能将生成式转化为生成器
next(a), a.__next__()  # 生成器的取值方式只能使用next的方法
def num():
        a, b = 0, 1
        for i in range(10):
                yield b   # 生成关键字yield，有yield的关键字的代码块就是yield的生成器。当运行到yield时代码就会停止，并返回运行结果，当在次运行是依旧是到yield时停止，并返回结果，
                                 # 生成器只能使用next方法
                a, b = b, a+b
                temp = yield b   # 这里并不是变量的定义，当运行到yield时就会停止，所以当运行到等号右边的时候就会停止运行，当再次使用next的时候，将会把一个None赋值给temp，
                                                # 因为b的值依旧在上轮循环中输出，这里可以使用num().send()方法将一个新的值赋值给temp
a = num()  # 将生成器赋值给变量a
for n in a:     # 生成器可以使用for循环使用，并且不会出错
        print(n)
# 注意：生成器占用内存小，在使用的时候取值，降低CPU和内存空间，提高效率。并且一般都使用for循环进行取值


# 迭代器
for i in '', [], (), {}, {:}
# 可以for循环的对象是可迭代对象
 a = (x for i in range(100))
 # 列表生成式，把中括号改为小括号就可以变为一个列表生成器，是可迭代对象
 for collections import Iterable 
 #如果想验证是否是可迭代对象，可以使用isinstance()判断是否是可迭代对象
 isinstance('abc', Iterable)
a = [1, 2, 3, 4, 5]
b = iter(a)  # 使用iter()方法可以将可迭代对象旋转为可迭代对象
# 注意：生成器是可迭代对象，迭代器不一定是生成器。并且迭代器无法回取，只能向前取值
# 注意：一个对象具有iter方法的才能称为可迭代对象，使用yield生成的迭代器函数，也有iter方法。凡是没有iter方法的对象不是可迭代对象，
#      凡是没有__next__()方法的不是生成器。(这里的方法都是魔法方法，是内置方法，可以使用dir()查看)


# 闭包
def num(num):
        def num_in(nim_in):
                return num + num_in  # 返回两个参数的和
        return num_in  # 返回内部函数的引用(变量名)
a = num(100)  # 将参数为100的函数num接收，并赋值给a，只不过这个返回值是一个函数的引用。等于a=num_in，
              # 注意这里接收的不光是函数本身，还有已经传递的参数
b = a(100)    # 调用函数a，即num_in，并传递一个参数100，返回值给b
# 注意：当一个函数定义在另一个函数内，且使用到了外部函数的参数，整个代码块称为闭包，当外部参数确定时，内部函数参数可以反复调用


# 装饰器
# 装饰没有参数的函数
def function(func):  # 定义了一个闭包
        def fun_in():  # 闭包内的函数
                print('这里是需要装饰的内容，就是需要添加的内容')
                func()  # 调用实参函数
        return func_in

def test():  # 需要被装饰修改的函数
        print('无参函数的测试')

test = function(test)  # 装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包
test()  # 这里再次调用test()的时候，其实是将会调用闭包内的函数func_in()。所以将会起到装饰修改的作用，最后会再次调用原函数test()

@function  # 装饰器的python写法，等价于test=function(test),并且无需调用当代码运行到这里，Python会自动运行
def test():
        print('无参函数的测试')
test()  # 这里再次调用函数是，将会产生修改后的效果



