BMI=float(input("请输入您的BMI："))
s=int(input("请输入您的性别：0为女生，其他数字为男生"))
if s==0:  #判断性别为“女”
    if 16.5<=BMI<=22.7:  #根据女生的标准进行判断（单分支）
        print("您的体重等级正常")  
else:
    if 16.5<=BMI<=23.2:  #根据男生的标准进行判断（单分支）
        print("您的体重等级正常") 
