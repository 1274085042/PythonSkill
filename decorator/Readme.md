装饰器的返回值也是一个函数  
# 简单装饰器  
```
def use_logging(func):
    def wrapper():
        print("%s is running" % func.__name__)
        func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()  
        #return func()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
```
装饰函数接受被装饰函数作为参数，里面写一个新函数代表新添加的功能，然后返回**被装饰函数**，再返回**新函数对象**  
# 语法糖
 @ 符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。  
```
def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()
```  
如上所示，有了 @ ，就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。因此，foo() 函数不需要做任何修改，只需在定义的地方加上装饰器，调用的时候还是和以前一样，如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

装饰器在 Python 使用如此方便都要归因于 Python 的**函数能像普通的对象一样能作为参数传递给其他函数**，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。  
# 带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器，在上面的装饰器调用中，该装饰器接收唯一的参数就是执行业务的函数 foo 。装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。这样，就为装饰器的编写和使用提供了更大的灵活性。比如，我们可以在装饰器中指定日志的等级，因为不同业务函数可能需要的日志级别是不一样的。
```
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator

#对装饰器decorator(func)具体化之后，再用装饰器对foo函数装饰。
@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()
```    
注:*args会把接收到的参数组成一个元组，**kwargs把接收到的键值对放入一个字典    

上面的 use_logging 是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。当我 们使用@use_logging(level="warn")调用的时候，Python 能够发现这一层的封装，并把参数传递到装饰器的环境中。

https://foofish.net/python-decorator.html