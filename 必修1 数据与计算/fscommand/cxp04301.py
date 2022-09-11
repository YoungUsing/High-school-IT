def match_num(num):   
    #该自定义函数实现计算一个数字需要多少根火柴棒




#以下为主程序   
snum=6	# 6根火柴棒
print("你可以拼出这些数字：")
for i in range(112):             
    if match_num(i)==snum: #如果i需要的火柴棒数等于现有火柴棒数
        print (i)

input("运行完毕，请按回车键退出...")
