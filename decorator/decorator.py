# a_string = 'this is a global scope'
# def foo(x):
#     a_string = 'ok'
#     print a_string
#     print 'locals',locals()
#     return 1
#
# print 'globals',globals()
#
# print foo(1)
# print a_string
#
#
# def foo1(x, y=0):
#     print x-y
#
# foo1(3,1)
# foo1(3)
# #foo()
# foo1(y=1,x= 10)
# #foo(a=10, b=1)

# def outer():
#     x=1
#     def inner():
#         print x
#     inner()
#
# outer()
# print issubclass(int, object)
#
# def pa():
#     pass
# print pa.__class__
# print issubclass(pa.__class__, object)
#
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def apply(func, x,y):
#     return func(x,y)
# print apply(add, 2,1)
# print apply(sub, 2,1)
#
# def outer():
#     x= 1
#     def inner():
#         print x
#     return inner
# foo = outer()
# print foo
# foo()

def outer(some_func):
    def inner():
        print 'before some function'
        ret = some_func()
        return ret + 1

    return inner


def foo():
    return 1


decorated = outer(foo)
print decorated
print decorated()


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #print self.__dict__

    def __repr__(self):
        return 'Coord: ' + str(self.__dict__)

def wrapper(func):
    def checker(a,b):
        if a.x <0 or a.y<0:
            a = Coordinate(a.x if a.x>0 else 0, a.y if a.y>0 else 0)
        if b.x <0 or b.y<0:
            b = Coordinate(b.x if b.x>0 else 0, b.y if b.y>0 else 0)
        ret = func(a,b)
        if ret.x <0 or ret.y<0:
            ret = Coordinate(ret.x if ret.x>0 else 0, ret.y if ret.y>0 else 0)
        return ret
    return checker

@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
# ob = add(two, one)
# print ob, ob.__dict__
#
# print sub(one, two)

print 'dsff'
#add = wrapper(add)
print add(one, three)
print 'dfsfdsf'
#sub = wrapper(sub)
print sub(one, two)

def one(*args):
    print args
one()
one(1,2,3,4)
def two(x, y, *args):
    print x,y, args

two('a','b','c')

def add(x,y, *args):
    print x, y, args
    return x+y
lst = [1,2,3,4]
print add(lst[0], lst[1])
print add(*lst)


def foo(**kwargs):
    print kwargs
foo()


foo(x=1, y=2)

dict = {'x': 1, 'y': 2}
def bar(x,y):
    return x+y
print bar(**dict)


def logger(func):
    def inner(*args, **kwargs):
        print 'arguments were: %s %s'%(args, kwargs)
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x*y

@logger
def foo2():
    return 2

print foo1(5,4)
print foo1(1)
print foo2()



