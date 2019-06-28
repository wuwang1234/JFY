import  pymysql


try:
    coon = pymysql.connect('localhost', 'root', 'Huawei@123', 'test')
    cursor = coon.cursor()

    # # # 使用 execute()  方法执行 SQL 查询
    # # cursor.execute("SELECT VERSION()")
    # cursor.execute("SELECT VERSION()")
    #
    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    #
    # print("Database version : %s " % data)

    # 查询
    SQL = 'select * from areas  limit 0,10;'
    cursor.execute(SQL)

    print('get one row data %s',cursor.fetchone())

    datas = cursor.fetchall()
    print('get all row datas %s',datas)

    #插入
    SQL = 'insert into students (name,gender) values("zhangqing001",0)'
    cursor.execute(SQL)
    coon.commit()


    #更新
    SQL='update students set gender=1 where name="zhangqing001"'
    cursor.execute(SQL)
    coon.commit()

    # 删除
    SQL='delete from students where name="zhangqing"'
    cursor.execute(SQL)
    coon.commit()

    cursor.close()

    # 关闭数据库连接
    coon.close()
except:
    print('e')
    pass

