#利用win32com.client模块的COM组件访问功能，通过ADODB访问Access的mdb文件
import win32com.client
conn = win32com.client.Dispatch(r"ADODB.Connection")  #建立数据库连接
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE =高二3D打印社团信息表.mdb'  
conn.Open(DSN)   #打开数据库

rs = win32com.client.Dispatch(r'ADODB.Recordset')   #打开一个记录集Recordset
tablename = '成员信息表'
rs.Open('[' + tablename + ']', conn, 1, 3)

while not rs.EOF:      #遍历记录，读取数据
    for i in range(rs.Fields.Count):
        print(rs.Fields[i].Name, ":", rs.Fields[i].Value)    #字段名：字段内容
    print(end='\n')
    rs.MoveNext()     #光标移到下条记录
print('该表有'+str(rs.Fields.Count)+'个字段')    
print('该表有'+str(rs.RecordCount)+'条记录')

#关闭连接
conn.Close()

