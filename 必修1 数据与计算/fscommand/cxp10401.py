def hanno(n,s,m,t):
    #定义一个函数,n层塔，将盘子从s借助m移动到t
    if n==1:
        print(s,'-->',t)   #将一个盘子从s移动到t
    else:
        hanno(n-1,s,t,m)   #将前n-1个盘子从s移动到m上
        print(s,'-->',t)    #将最底下的最后一个盘子从s移动到t上
        hanno(n-1,m,s,t)   #将m上的n-1个盘子移动到t上
#主程序
n=int(input('请输入汉诺塔的层数：'))
hanno(n,'A','B','C')
input("运行完毕，请按回车键退出...") 
