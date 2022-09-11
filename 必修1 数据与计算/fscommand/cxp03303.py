age=float(input('请输入age='))
HRrest=float(input('请输入HRrest='))
EHR=float(input('请输入EHR=')) #输入运动后的心率
gender=input("请输入male or female :")
if gender=='male':
  n=220
else:
  n=210
low=(n-age-HRrest)*0.6+HRrest
high=(n-age-HRrest)*0.8+HRrest
if EHR<low:
  print('您的运动心率太低，请适当提高')
elif low<=EHR<=high:
  print('您的运动心率正好，请保持')
else:
  print('您的运动心率太高，请适当降低')
input("运行完毕，请按回车键退出...")
