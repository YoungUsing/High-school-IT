from tkinter import *
root = Tk()                         #创建一个窗口        
root.title("添加线路")              #设置窗口标题
root.geometry('600x100')            #设置窗口大小
root.resizable(0,0)                 #禁止调整窗口大小
var=StringVar()                     #定义StringVar()类型

def intomap():                      #Button按钮激发函数
    c=open("旅行线路.txt",'a+')     #以追加模式打开文件
    c.write(var.get()+"\n")         #在文件末尾添加text里的内容
    c.close                         #关闭文件

#在窗口上建一个文本标签
Label(root, text='请输入线路', font=('Arial', 10)).pack()
#在窗口上建一个文本框
Entry(root,textvariable=var,width=550).pack()
#在窗口上建一个Button按钮
Button(root, text="添加线路", command =intomap,relief="solid",width=10).pack()
root.mainloop()
