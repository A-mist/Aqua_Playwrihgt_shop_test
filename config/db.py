import pymysql


def db_localhost_mysql():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='test',
    )
    cur = conn.cursor()
    return cur

def db_test_mysql():
    conn = pymysql.connect(
        host='ibi-power-test8.mysql.rds.aliyuncs.com',
        port=3306,
        user='dd_user',
        passwd='27gRb89Fwrd&eWdxh91P_R0ZLjgDJQ',
        database='test_toodudu',
    )
    cur = conn.cursor()
    return cur
