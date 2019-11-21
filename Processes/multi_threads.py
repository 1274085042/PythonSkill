#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

import time,threading,multiprocessing

#新线程执行的代码
# def loop():
#     print('thread %s is running...'%threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print("thread %s >>> %s"%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.'%threading.current_thread().name)
#
# print('thread %s is runing...'%threading.current_thread().name)
# t=threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended'%threading.current_thread().name)

'''由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，
子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
如果不起名字Python就自动给线程命名为Thread-1，Thread-2……'''


'''
一、Lock
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

来看看多个线程同时操作一个变量怎么把内容给改乱了：
'''
#假定这是你的银行存款
# balance=0
# def change_it(n):
#     global balance
#     balance=balance+n
#     balance=balance-n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

'''
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，
当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

balance = balance + n
也分两步：

计算balance + n，存入临时变量中；
将临时变量的值赋给balance。
也就是可以看成：

x = balance + n
balance = x
由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：

初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5
t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8
t2: x2 = balance - 8  # x2 = 8 - 8 = 0
t2: balance = x2      # balance = 0
结果 balance = 0

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：

初始值 balance = 0

t1: x1 = balance + 5   # x1 = 0 + 5 = 5

t2: x2 = balance + 8   # x2 = 0 + 8 = 8
t2: balance = x2       # balance = 8

t1: balance = x1       # balance = 5
t1: x1 = balance - 5   # x1 = 5 - 5 = 0
t1: balance = x1       # balance = 0

t2: x2 = balance - 8   # x2 = 0 - 8 = -8
t2: balance = x2       # balance = -8
结果 balance = -8

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
'''

'''
如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，
同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
'''
# balance=0
# lock=threading.Lock()
#
# def change_it(n):
#     global balance
#     balance=balance+n
#     balance=balance-n
#
# def run_thread(n):
#     for i in range(100000):
#         #先要获取锁
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             #改完之后一定要释放锁
#             lock.release(
#
#             )
#
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

'''
二、多核CPU

'''
def loop():
    x=0
    while True:
        x=x^1

for i in range(multiprocessing.cpu_count()):
    t=threading.Thread(target=loop)
    t.start()














