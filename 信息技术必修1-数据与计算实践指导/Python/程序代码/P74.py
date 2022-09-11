from tkinter import *
root = Tk()                         #创建一个窗口        
root.title("旅行线路")              #设置窗口标题
root.geometry('300x120')            #设置窗口大小
root.resizable(0,0)                 #禁止调整窗口大小

#在窗口上建一个Button按钮
Button(root, text="添加线路", relief="solid",width=10,height=2).pack()
Button(root, text="查询线路", relief="solid",width=10,height=2).pack()

