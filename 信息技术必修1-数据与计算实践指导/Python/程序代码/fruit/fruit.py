# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:27:34 2020

@author: chenxiaohong
"""

import random
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN="Provider=Microsoft.Jet.OLEDB.4.0;Data Source=fruit.mdb;"

conn.Open(DSN)
#打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
tablename = '水果清单'
rs.Open('[' + tablename + ']', conn, 1, 3)
#遍历记录，读取数据
#rs.MoveFirst()  #光标移到首条记录
fruit_num=[]#水果编号
fruit_name=[]#水果名称
fruit_weight=[] #水果重量
fruit_price=[]#水果价格
#sum=0 #水果总数
while not rs.EOF:
    i=0
    while i<rs.Fields.Count:
        fruit_num.append(rs.Fields[i].Value)
        fruit_name.append(rs.Fields[i+1].Value)
        fruit_weight.append(rs.Fields[i+2].Value)
        fruit_price.append(rs.Fields[i+3].Value)
        i=i+4
    rs.MoveNext()     #光标移到下条记录
    #sum=sum+1
conn.Close() #关闭连接
#print(sum)
print("***社区超市水果清单***")
print("%-6s %6s %10s"%("水果名称","重量","价格"))
for i in range(len(fruit_num)):
    print("%-6s %8d %14.2f"%(fruit_name[i],fruit_weight[i], fruit_price[i]))
i=0
print("\n你可以选择的水果为")
print("%-4s %-6s %6s %10s"%("编号","水果名称","重量","价格"))
rand_num=[]#随机产生的水果
list_num=[]
list_fruit=[]
list_price=[]
list_weight=[]
list_binary=[]
#随机产生5种水果并输出
while i<5: 
    x=random.randint(0,len(fruit_num)-1)
    #print(x)
    if x not in rand_num:
        rand_num.append(x)
        list_num.append(i)
        list_fruit.append(fruit_name[x])
        list_weight.append(fruit_weight[x])
        list_price.append(fruit_price[x])
        print("%-6d %-8s %6d %14.2f"%(i,fruit_name[x],fruit_weight[x],fruit_price[x]))
        i=i+1

max_weight=float(input("\n输入最大允许购买重量："))

#根据随机选择的5种水果和最大允许购买重量，计算最优购买方案
max_price=0.0
for i in range(5):    
    if list_price[i]>max_price and list_weight[i]<=max_weight:
       list_binary=[]
       max_price=list_price[i]
       list_binary.append(i)
for i in range(5):
    for j in range(5):
        if  i!=j :
            weight=list_weight[i]+list_weight[j]
            price=list_price[i]+list_price[j]
            if price>max_price and weight<=max_weight:
                list_binary=[]
                max_price=price
                list_binary.append(i)
                list_binary.append(j)
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i!=j and i!=k and j!=k:
                weight=list_weight[i]+list_weight[j]+list_weight[k]
                price=list_price[i]+list_price[j]+list_price[k]
                if price>max_price  and weight<=max_weight:
                    max_price=price
                    list_binary=[]
                    list_binary.append(i)
                    list_binary.append(j)
                    list_binary.append(k)
print("\n最佳购买方案为")
print("%-4s %-6s"%("编号","水果名称"))
for i in list_binary:
    #print(i,list_price[i],list_fruit[i],end='\t')
    print("%-6d %-8s" %(i,list_fruit[i]))
print(end='\n')
print("最高价格为：%.2f"%(max_price))

#根据顾客的选择情况，进行结算最后的价格
cus_fruit=[]
cus_price=0.0
in_fruit=int(input("请输入您选择的水果信息(输入-1表示输入结束）："))
while in_fruit!=-1:
    cus_fruit.append(in_fruit)
    cus_price+=list_price[in_fruit]
    in_fruit=int(input())
print("您选择的水果为：")

for i in cus_fruit:
    print(list_fruit[i],end='\t')
print(end='\n')
if cus_fruit==list_binary:
    print("您可以打对折，请付款：%.2f"%(0.5*max_price))
else:
    print("您可以打八折，请付款：%.2f"%(0.8*cus_price))

