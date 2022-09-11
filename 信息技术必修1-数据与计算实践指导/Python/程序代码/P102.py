max_weight=float(input("输入允许购买的最大质量："))
max_price=0.0
for i in range(5):
    for j in range(5):
        if i!=j:
            weight=list_weight[i]+list_weight[j]
            price=list_price[i]+list_price[j]
            if price>max_price and weight<=max_weight
                list_binary=[]
                max_price=price
                list_binary.append(i)
                list_binary.append(j)
for i in range(5):
    for j in range(5):
        for k in range(5):
