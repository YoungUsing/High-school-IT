encry_data=[]
raw_data=[]
n=int(input("输入加密的数据量n:"))
m=int(input("输入数段长度m:"))
print("输入加密后的数据列表：")
for i in range(n):
    x=int(input())
    encry_data.append(x)

for i in range(n//m):
    for j in range(m):
        y=encry_data[i*m+j]//100*32+encry_data[i*m+j]%100
        raw_data.append(y)

for i in range(n-1,n//m*m-1,-1):
    raw_data.append(encry_data[i])
print(raw_data)
    
    
