import random
num=random.randint(1,100)
mynum=int(input('请输入mynum='))
n=1
while not(num==mynum):
    n=n+1
    print("输入不正确,请再次输入")
    mynum=int(input('请输入mynum='))
print("你猜对了！","一共用了",n,"次")

  
input("运行完毕，请按回车键退出...")
