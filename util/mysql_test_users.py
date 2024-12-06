from util.data_cleaning import date_cleaning_name
from config.db import db_test_mysql


def get_all_names(name):
    sur=db_test_mysql()
    sur.execute('select * from users where user_name=%s', (name))
    rows = sur.fetchall()
    return date_cleaning_name(rows)


if __name__ == '__main__':
    print(get_all_names('李龙威'))
