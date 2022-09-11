import random
s=0
while s!=1:
    s=int(input("请输入掷色子的次数："))
    cishu=0  #记录“6点”出现的“次数”
    for i in range(s):
        num1=random.randint(1,6)
        if num1==6:
            cishu=cishu+1

    print(cishu/s)
print("退出游戏")
