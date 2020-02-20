#coding=utf-8

import logging

# def use_logging(func):
#     logging.warning('%s is running' %func.__name__)
#     func()
#
# def foo():
#     print('I am foo')
#
# use_logging(foo)


# def use_logging(func):
#     def warpper():
#         print('%s is running' %func.__name__)
#         #logging.warning('%s is running' %func.__name__)
#         func()
#         #return func()
#     return warpper
# @use_logging
# def foo():
#     print('I am foo')
#
# # foo=use_logging(foo)  #因为装饰器use_logging(foo)返回函数warpper,这条语句相当于foo=wrapper
#   foo()                 #执行foo()相当于执行wrapper()


def use_logging(level):
    def decorator(func):
        def warpper(*k,**kw):
            if level=='warn':
                logging.warning('%s is running'%func.__name__)
            elif level=='info':
                logging.info('%s is running'%func.__name__)

            return func(*k)
        return warpper
    return  decorator
@use_logging('warn')
def foo(name='foo'):
    print('I am %s'%name)
foo('foo__')