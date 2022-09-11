import win32com.client
conn=win32com.client.Dispatch(r"ADODB.Connection")
DSN='PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=fruit.mdb'
#Access 2007及以后版本
#DSN='PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=fruit.mdb'
#Access 2007以前版本
conn.Open(DSN)   #打开一个记录集Recordset
rs=win32com.client.Dispatch(r"ADODB.Connection")
tablename='水果清单'
rs.Open('['+tablename+']',conn,1,3)
fruit_num=[]
fruit_name=[]
fruit_weight=[]
fruit_price=[]
while not rs.EOF:
    i=0
    while i<rs.Fields.Count:
        fruit_num.append(rs.Field[i].Value)
        fruit_num.append(rs.Field[i+1].Value)
        fruit_weight.append(rs.Field[i+2].Value)
        fruit_price.append(rs.Fields[i+3].Value)
        i=i+4
    rs.MoveNext()
conn.Close()
