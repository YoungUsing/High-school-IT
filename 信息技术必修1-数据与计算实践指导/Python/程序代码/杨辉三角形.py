def yang_h(x):
    line = [1]    # 第一行就一个元素1
    print(line)
    for i in range(1,x):
        temp = []   #当前行数列初始化
        for j in range(len(line)-1): 
            temp.append(line[j]+line[j+1])  #当前行数列的值为上一行数列与其相对位置和后一位置数的和
        line=[1]+temp+[1]  #对新产生的数列首尾增加1
        print(line)

n=int(input("请输入三角形规模："))
yang_h(n)
