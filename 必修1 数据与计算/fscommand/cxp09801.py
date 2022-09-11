def fib(n):
    #迭代求Fibonacci数列
    f2=f1=1
    for i in range(3,n+1):
        f1,f2=f2,f1+f2
    return f2
n=int(input('输入需要计算的月份数：'))
print('兔子总对数为：',fib(n))
input("运行完毕，请按回车键退出...")
