from config.db import db_localhost_mysql
from util.data_cleaning import date_cleaning_name


def get_all():
    cur = db_localhost_mysql()
    cur.execute(f"select user_name from user")
    rows = cur.fetchall()
    cur.close()
    return date_cleaning_name(rows)

def get_name(key):
    cur = db_localhost_mysql()
    cur.execute(f"select user_name from user where user_name = '{key}'")
    rows = cur.fetchall()
    cur.close()
    return date_cleaning_name(rows)

if __name__ == '__main__':
    print(get_name('李龙威'))
