   
-   **pytorch/**
    -   **distributed/**
        -   **tensor/**
            -   **experimental/**
                -   `_attention.py`: 定义customized_ops、context_parallel   
                -   `__init__.py`: experimental模块的初始化，导出了 `context_parallel` 函数
            -   `__init__.py`
        -   `__init__.py`

        -   **_tensor/**
            -   `__init__.py`: 由于一些代码移入了pytorch.distributed.tensor，为了backward compatibility，保持以`_tensor`开头的旧导入路径依然有效，因此该文件作为一个shim将_tensor重定向到tensor
       
    -   `__init__.py`


-   **torch_mlu/**
    -   **distributed/**
        -   **tensor/**
            -   `_attention.py`: 对pytorch.distributed.tensor.experimental._attention中的customized_ops做修改   
            -   `__init__.py`
        -   `__init__.py`
    -   `__init__.py`

-   `test.py`: 测试脚本  


该project展示使用importlib.import_module(...)出错的情况：   
在test.py中 
- import torch_mlu   
这会修改pytorch.distributed.tensor.experimental._attention中的customized_ops    
- from pytorch.distributed._tensor.experimental._attention import context_parallel    
通过import_module将pytorch.distributed._tensor.experimental重定向为pytorch.distributed.tensor.experimental，但是在倒入context_parallel时，_attention中的customized_ops又新创建了一次  

# 总结  
模块A  
```python  
import A  
importlib.import_module(A)  # 这会导致A中的全局代码可能再执行一遍
```
