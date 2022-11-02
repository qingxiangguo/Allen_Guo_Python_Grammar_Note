# Qingxiang Guo
# {2022/6/4} {15:19}
'''
这里介绍python包的基本用法，
实际开发中，一个大型的项目往往需要使用成百上千的 Python 模块，如果将这些模块都堆放在一起，势必不好管理。而且，
使用模块可以有效避免变量名或函数名重名引发的冲突，但是如果模块名重复怎么办呢？因此，Python提出了包（Package）的概念。
模块就是.py文件，那什么是包呢？简单理解，包就是文件夹，只不过在该文件夹下必须存在一个名为“__init__.py” 的文件。
每个包的目录下都必须建立一个 __init__.py 的模块，可以是一个空模块，可以写一些初始化代码，其作用就是告诉 Python 要将该目录当成包来处理。
注意，__init__.py 不同于其他模块文件，此模块的模块名不是 __init__，而是它所在的包名。例如，在 settings 包中的 __init__.py 文件，其模块名就是 settings。
包是一个包含多个模块的文件夹，它的本质依然是模块，因此包中也可以包含包。
'''

#建立一个test_package1，并且在本模块中导入test_package1包

import test_package1.module_A as ma  #ma是test_package1这个模块的别名
print(ma.a)  #输出10

#使用import方式进行导入时，只能跟包名或模块名
import test_package1   #这是个包（目录）
import calc   #这是个模块（文件）

#使用from...import可以导入包，模块，函数，变量
from test_package1 import module_A   #从包导入模块，最后导入的是模块
from test_package1.module_A import a   #从包的模块导入，最后导入的是变量

