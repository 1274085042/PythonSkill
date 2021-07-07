#coding=utf-8
import os,time,random
'''
一、 子进程只需要调用getppid()就可以拿到父进程的ID
getpid获取当前进程ID
'''
#print("Processes (%s) start..."% os.getpid())

'''
二、multiprocessing模块提供了一个Process类来代表一个进程对象，
'''
# from multiprocessing import Process
# def run_proc(name):
#     print('Run child process %s (%s)'%(name,os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#
#     #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
#     p=Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#
#     #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     p.join()
#     #print('Child process end.')

'''
三、如果要启动大量的子进程，可以用进程池的方式批量创建子进程
'''
# from multiprocessing import Pool
#
# def long_time_task(name):
#     print('Run task %s (%s)...'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Task %s run %0.2f seconds.'%(name,(end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s.'%(os.getpid()))
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print("Waiting for all subprocesses done...")
#     p.close()
#     p.join()
#     print('All subprocesses done.')

'''
注意输出的结果，task 0,1,2,3是立刻执行的，而task 4要等待前面某个task完成后
才执行，这是因为Pool的默认大小为4，因此最多同时执行4个进程。这是Pool有意设计
的限制，并不是操作系统的限制。如果改成：
p = Pool(5)
就可以同时跑5个进程。
'''

'''
四、subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)
'''
如果子进程还需要输入，则可以通过communicate()方法输入
'''

'''
五、进程间的通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的
multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，
一个从Queue里读数据：
'''
from multiprocessing import Process, Queue
'''
1、两个子进程之间进程通信
'''
#写数据进程执行的代码
# def write(q):
#     print('Process to write:%s'%os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...'%value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('Process to read:%s'%os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s from queue.'%value)
#
# if __name__=='__main__':
#     #父进程创建Queue，并传给各个子进程
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#
#     #启动子进程pw，写入
#     pw.start()
#     #启动子进程pr,读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()

'''
2、主进程和子进程之间进行通信
'''
def foo(q):
    s=q.get()
    print("子进程受到的数据：")
    print(s)

if __name__=='__main__':
    q=Queue()
    p=Process(target=foo,args=(q,))
    p.start()

    print("主进程准备发送数据...")
    q.put("有内鬼，终止交易！")
    p.join()