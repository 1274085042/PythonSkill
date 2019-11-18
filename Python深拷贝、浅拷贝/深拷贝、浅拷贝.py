#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

'赋值'
# m = [1, 2, [3, 4], [5, [6, 7]]]
# print('m:', id(m))
# print([id(i) for i in m])
# n = m
# print('n:', id(n))
# print([id(i) for i in n])
# print(n is m)
# print(n[0] is m[0])
# print(n[2] is m[2])
# n[0] = -1
# print(m)
# n[2][1] = -1
# print(m)

'浅拷贝'
from copy import  copy
m = [1, 2, [3, 4], [5, [6, 7]]]
print('m:', id(m))
print([id(i) for i in m])
n=copy(m)
print('n:', id(n))
print([id(i) for i in n])
print(n is m)
print(n[0] is m[0])
print(n[2] is m[2])
n[0] = -1
print(m)
n[2][1] = -1
print(m)
print(n)

'深拷贝'
from copy import deepcopy
a = [3, 4]
m = [1, 2, a, [5, a]]
n = deepcopy(m)
n[3][1][0] = -1
print(n)
