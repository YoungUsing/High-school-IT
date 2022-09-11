b=''
d=int(input('请输入非负整数d='))
while d>0:
    r=d%2
    b=str(r)+b
    d=d//2
if b=='':
    b='0'
print(b)
print()
input("运行完毕，请按回车键退出...")
