#水仙花数是指一个 3 位数，
#它的每个位上的数字的 3次幂之和等于它本身(例如:1^3 + 5^3+ 3^3 = 153)。

def sxhs(a):
  g=a%10
  s=a//10%10
  b=a//100
  if g**3+s**3+b**3==a:
    return True
  else:
    return False 
 
for i in range(100,999):
    if sxhs(i):
      print(i)
