﻿champion=['A','B','C','D'] #设置选手列表
for i in champion: #循环读取选手编号
    cond=(i!='A') +(i=='C') + (i=='D')+(i!='D') #查找符合条件的选手
    if cond==3: #说真话是否是3人
        print("冠军是:",i) #输出冠军
input("运行完毕，请按回车键退出...") 
