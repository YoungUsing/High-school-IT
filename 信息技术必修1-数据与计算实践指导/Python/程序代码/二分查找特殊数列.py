list_data=[3,7,13,25,39,2,8,10,16,50]
list_len=len(list_data)
key=int(input("输入需要查找的关键字"))
i=0
j=list_len-1
while(i<=j):
        m=(i+j)//2
        if key%2==1 and list_data[m]%2==0:
            j=m-1
        elif key%2==0 and list_data[m]%2==1:
            i=m+1
        else:
            if key<list_data[m]:
                j=m-1
            elif key>list_data[m]:
                i=m+1
            else:
                print("找到该数，在数列第",m+1,"个位置")
                break
                
if i>j:
    print("数列中没有该数！")
    
        
