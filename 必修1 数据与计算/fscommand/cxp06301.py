def dfs(v,vis):
  global min,s,r,minr
  vis.add(v)
  r=r+'-'+v
  if vis==set('HABC'):
    s=s+G[v]['H']
    r=r+'-'+'H'
    print('线路'+r[1:]+'用时:'+str(s))
    if s<min:
      min=s
      minr=r
    s=s-G[v]['H']
    r=r[:-2]
  else:
    for u in G[v]:
      if u not in vis:
        s=s+G[v][u]
        dfs(u,vis)
        vis.remove(u)
        s=s-G[v][u]
        r=r[:-2]
  return min

G={'H':{'A':2,'B':5,'C':10},'A':{'H':2,'B':4,'C':6},'B':{'H':5,'A':4,'C':4},'C':{'H':10,'A':6,'B':4}}
min=999
s=0
r=''
minr=''
print("最短用时:"+str(dfs('H',set())))
print("最短用时线路有:"+minr[1:])

print()
input("运行完毕，请按回车键退出...")
