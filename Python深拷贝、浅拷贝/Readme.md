m = [1, 2, [3, 4], [5, [6, 7]]]  
图示：  
![][image1]    
### 1、赋值  
n=m  
这样的赋值语句相当与C++的引用   

![][image2]  
  
### 2、要想得到一个对象的“拷贝”，我们需要用到copy方法：  
`from copy import copy`  
`n=copy(m)   #只拷贝父对象，不拷贝子对象`    

![][image3]    

### 3、要彻底地产生一个和原对象完全独立的复制品，得使用 深拷贝 （ deep copy ）：  
`from copy import deepcopy`  
`n=deepcopy(m)`    

此时， 对新对象中元素做任何改动都不会影响原对象 。  
![][image4]

[//]: # (image reference)  
[image1]: ./example/1.png  
[image2]: ./example/2.png  
[image3]: ./example/3.png
[image4]: ./example/4.png

