import random
i=0
rand_num=[]
list_name=[]
list_weight=[]
list_price=[]
list_binary=[]

while i<5:  #随机产生5种水果并输出
    x=random.randint(1,len(fruit_num-1))
    if x not in rand_num:  #随机获取的水果的编号不在已有编号中则加入
        rand_num.append(x)
        list_name.append(fruit_name[x])
        list_weight.append(fruit_weight[x])
        list_price.append(fruit_price[x])
        print(fruit_name[x]," ",fruit_weight[x]," ",fruit_price[x])
        i=i+1
