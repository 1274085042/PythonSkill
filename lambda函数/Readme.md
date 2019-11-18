lambda函数是一个匿名函数，用`lambda`关键字定义，后面紧跟lambda参数，lambdas表达式位于冒号的右侧。表达式的结果将最终成为lambda函数的返回值.  
  
`lambda argument_list: expression`    

用法：    

1、**将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。**   
例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1,2)，输出为3。    
  
2、**将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。**  
例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：time.sleep=lambda x:None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。  
  
3、**将lambda函数作为其他函数的返回值，返回给调用者。**  
  
4、**将lambda函数作为参数传递给其他函数。**  
lambda函数通常和以下Python内置函数一起使用  
* Filter: filter (lambda parameter: expression, iterable-sequence)
* Map: map (lambda parameter: expression, iterable-sequences)
* Reduce: reduce (lambda parameter1, parameter2: expression, iterable-sequence)  
       
[**Code**](lambda_func.py)
