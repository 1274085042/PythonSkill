#coding=utf-8

'一、将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。'
add=lambda x,y: x+y
print( add(1,2) )


'二、将lambda函数赋值给其它函数，从而将其它函数用该lambda函数替换。'
def mautal(x,y):
    return x*y
mautal=lambda x,y : x**y
print(mautal(3,2))

'一、二都是将lambda函数变成了一个有名函数'


'三、将lambda函数作为其它函数的返回值，返回给调用者'
def myfunc(n):
    return lambda a:a*n
mydouble=myfunc(2)
print(mydouble(11))


'四、将lambda函数作为参数传递给其它函数'
#1、filter函数
#（1）lambda表达式计算该数字是奇数还是偶数，并相应地返回true或false。
#只有在lambda函数中被赋值为true的值才会被包含在filter()函数创建的迭代结果中。
#print(filter(lambda x:x%2==0,range(0,11)))
filtered=[i for i in  filter(lambda x:x%2==0,range(0,11))]
print(filtered)

#（2）移除列表中的空字符
filtered=list(filter(lambda x:len(x.strip())>0,['str','','le','    ','','qin']))
print(filtered)

#2、map函数
# lambda函数对列表中的每一个元素进行表达式运算。
mapped=list(map(lambda x:x+1,[2,3,4]))
print(mapped)

#3、sorted函数

#4、reduce函数
#reduce函数与map()类似，用于对序列中的每个元素应用一个操作。然而，它与map的工作方式不同。下面是reduce()函数计算输出的步骤:
#（1）对序列的前两个元素执行定义的操作。
#（2）保存结果
#（3）使用保存的结果和序列中的下一个元素执行定义操作。
#（4）重复此操作，直到不再剩下任何元素。
from  functools import reduce
sequences=[1,2,3]
result=reduce(lambda x,y:x*y , sequences)
print(result)