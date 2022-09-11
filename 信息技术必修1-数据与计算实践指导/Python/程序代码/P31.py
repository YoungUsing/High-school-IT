w=float(input("请输入体重（kg）=")) #输入浮点型数据
h=float(input("请输入身高（m）=")) #仿照第一句的格式填写
BMI=w/(h*h)
SW=22*(h*h)
#保留2位小数
print("BMI=",format(BMI,".2f"),"标准体重=",format(SW,".2f"))

