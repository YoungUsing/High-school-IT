def InsertQ(x,i):
  global rear
  if x not in Q:
    rear+=1
    Q.append(x)
    F.append(front)
    L.append(i)

def OutputR(front):
  global n
  if F[front]>0:
    OutputR(F[front])
  if L[front]>=0:
    n+=1
    print("第"+str(n)+"步:"+law[L[front]])

def OK(M,W,S,V):
  return W!=S and S!=V or M==S

Q=[0];F=[0];L=[-1]
law=["移动人","移动人和狼","移动人和羊","移动人和菜"]
front=0;rear=0
while front<=rear:
  x=Q[front]
  if x==15:
    break
  V=x%2
  S=x//2%2
  W=x//4%2
  M=x//8
  if OK(1-M,W,S,V):
    x=(1-M)*8+W*4+S*2+V
    InsertQ(x,0)
  if M==W and OK(1-M,1-W,S,V):
    x=(1-M)*8+(1-W)*4+S*2+V
    InsertQ(x,1)
  if M==S and OK(1-M,W,1-S,V):
    x=(1-M)*8+W*4+(1-S)*2+V
    InsertQ(x,2)
  if M==V and OK(1-M,W,S,1-V):
    x=(1-M)*8+W*4+S*2+(1-V)
    InsertQ(x,3)
  front+=1
if x==15:
  print("人狼羊菜过河游戏成功！")
  n=0
  OutputR(front)
else:
  print("无法完成任务！")

print()
input('运行结束，按回车键退出...')
