from distutils.core import setup
setup(  
    name ='mymodule',                  #参数一定要与mymodule.py文件名相同
    version ='1.0.0',                        #版本号
    py_modules  =['mymodule'],    #参数一定要与mymodule.py文件名相同
    author='yd',                               #作者
    author_email='zy@mail.com',  #作者邮箱
    description ='计算一个数字需要多少根火柴棒',  #代码功能描述
    )  
