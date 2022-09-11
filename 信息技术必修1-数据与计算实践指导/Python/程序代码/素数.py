import math
for m in range(101,201,2):
    k=int(math.sqrt(m))    
    for i in range(2,k+1):        
        if m%i==0:
            break
    if i==k:
        print(m)
        
