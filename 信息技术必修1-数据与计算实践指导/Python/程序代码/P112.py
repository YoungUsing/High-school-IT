import numpy as np
import matplotlib.pyplot as plt
import math
n=int(input("请输入数据规模："))
x=np.arange(0.05,n,0.5)+0.5
f1=[math.log(i,2) for i in x]
f2=x
f3=x**2
f4=np.power(2,x)
#创建多子图形式
plt.figure(1)
plt.title("Time complexity analysis of the algorithm")
ax1=plt.subplot(2,2,1) #第1行第1列图形
ax2=plt.subplot(2,2,2) #第1行第2列图形
ax3=plt.subplot(2,2,3) #第2行第1列图形
ax4=plt.subplot(2,2,4) #第2行第2列图形
plt.sca(ax1)
plt.plot(x,f1,label='O(log2n)')
plt.legend()
plt.sca(ax2)
plt.plot(x,f2,label='O(n)')
plt.legend()
plt.sca(ax3)
plt.plot(x,f3,label='O(n^2)')
plt.legend()
plt.sca(ax4)
plt.plot(x,f4,label='O(2^n)')
plt.legend()
plt.show()
#创建单图形式
plt.figure(2)
x=np.arange(0.05,n,0.5)+0.5
plt.plot(x,f1,label='O(log2n)')
plt.plot(x,f2,label='O(n)')
plt.plot(x,f3,label='O(n^2)')
plt.plot(x,f4,label='O(2^n)')
plt.legend()
plt.title("Time complexity analysis of the algorithm")
plt.show()
print('')
print('算法时间复杂度数值分析')
print('f(log2n)f(n)f(n^2)f(2^n)',)
print('当n=4',' ',math.log(4,2),'',4,'',4**2,'',2**4)
print('当n=10',' ',math.log(10,2),' ',10,' ',10**2,' ',2**10)
print('当n=100',' ',math.log(100,2),' ',100,' ',100*2,' ',2**100)
print('当n=1000',' ',math.log(1000,2),' ',1000,'',1000*2,'',2**1000)
