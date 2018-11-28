import cx_Oracle       #引用模块cx_Oracle


def main():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')  # 连接数据库
    c = conn.cursor()  # 获取cursor
    x = c.execute('select sysdate from dual')  # 使用cursor进行各种操作
    x.fetchone()
    url = "http://www.du871.com/index-show-iNWlERWAJQA9nA75PKMx1HelbE8_3D.htm"
    is_or_not = 1
    sql = """insert into spider(l_id,vc_url,vc_name,l_isonline, d_date) values(3, :1, 2, :2, sysdate)"""
    c.execute(sql.encode("utf-8"), [url, is_or_not])
    conn.commit();
    print(sql)
    c.close()  # 关闭cursor
    conn.close()  # 关闭连接

if __name__ == '__main__':
    main()