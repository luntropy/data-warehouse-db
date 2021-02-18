#!/usr/bin/python3

from modules.connection import Connection

def prepare_data(data):
    prepared = []
    for i in data:
        if not i:
            val = 'NULL'
            prepared.append(val)
        elif i != ' ':
            if not isinstance(i, str):
                i = str(i)

            val = "'" + i + "'"
            prepared.append(val)

    return tuple(prepared)

def fill_dim_order_type(con, con_dw):
    order_types = '''SELECT k_symbol FROM permanent_order GROUP BY k_symbol;'''

    res = None
    with con.cursor() as curs:
        curs.execute(order_types)
        res = curs.fetchall()

    for i in res:
        prepared = prepare_data(i)

        if prepared:
            fill_order_types = '''INSERT INTO dim_order_type (type) VALUES ({0});'''.format(prepared[0])

            with con_dw.cursor() as curs:
                curs.execute(fill_order_types)
                con_dw.commit()

def fill_dim_order(con, con_dw):
    order_info = '''SELECT bank_to, account_to FROM permanent_order GROUP BY bank_to, account_to;'''

    res = None
    with con.cursor() as curs:
        curs.execute(order_info)
        res = curs.fetchall()

    for i in res:
        prepared = prepare_data(i)

        if prepared:
            fill_order_info = '''INSERT INTO dim_order (bank_to, account_to) VALUES ({0}, {1});'''.format(prepared[0], prepared[1])

            with con_dw.cursor() as curs:
                curs.execute(fill_order_info)
                con_dw.commit()

def fill_dim_account(con, con_dw):
    query = '''SELECT creation_date, frequency FROM accounts GROUP BY creation_date, frequency;'''

    res = None
    with con.cursor() as curs:
        curs.execute(query)
        res = curs.fetchall()

    for i in res:
        prepared = prepare_data(i)

        if prepared:
            fill_acc_info = '''INSERT INTO dim_account (creation_date, frequency) VALUES ({0}, {1});'''.format(prepared[0], prepared[1])

            with con_dw.cursor() as curs:
                curs.execute(fill_acc_info)
                con_dw.commit()

def fill_dim_year(con, con_dw):
    for i in range(1993, 1999):
        value = "'" + str(i) + "'"

        fill_years = '''INSERT INTO dim_calendar_year (year) VALUES ({0});'''.format(value)

        with con_dw.cursor() as curs:
            curs.execute(fill_years)
            con_dw.commit()

def fill_dim_month(con, cond_dw):
    for i in range(1993, 1999):
        year = "'" + str(i) + "'"

        query = '''SELECT year_id, year FROM dim_calendar_year WHERE year = {0}'''.format(year)

        res = None
        with con_dw.cursor() as curs:
            curs.execute(query)
            res = curs.fetchall()

        for i in res:
            year_id = "'" + str(i[0]) + "'"
            year = "'" + str(i[1]) + "'"

            for j in range(1, 13):
                month_name = 'NULL'

                if j == 1:
                    month_name = "'January'"
                elif j == 2:
                    month_name = "'February'"
                elif j == 3:
                    month_name = "'March'"
                elif j == 4:
                    month_name = "'April'"
                elif j == 5:
                    month_name = "'May'"
                elif j == 6:
                    month_name = "'June'"
                elif j == 7:
                    month_name = "'July'"
                elif j == 8:
                    month_name = "'August'"
                elif j == 9:
                    month_name = "'September'"
                elif j == 10:
                    month_name = "'October'"
                elif j == 11:
                    month_name = "'November'"
                elif j == 12:
                    month_name = "'December'"

                fill_months = '''INSERT INTO dim_calendar_month (month_number, month_name, year_id, year) VALUES ({0}, {1}, {2}, {3});'''.format(str(j), month_name, year_id, year)

                with con_dw.cursor() as curs:
                    curs.execute(fill_months)
                    con_dw.commit()

def fill_dim_date(con, con_dw):
        query = '''SELECT t.day::date FROM generate_series(timestamp '1993-01-01', timestamp '1998-12-31', interval '1day') as t(day);'''

        with con_dw.cursor() as curs:
            curs.execute(query)
            res = curs.fetchall()

        for i in res:
            date = "'" + str(i[0]) + "'"

            fill_dates = '''INSERT INTO dim_calendar_date (calendar_date) VALUES ({0});'''.format(date)

            with con_dw.cursor() as curs:
                curs.execute(fill_dates)
                con_dw.commit()

def fill_dim_district(con, con_dw):
    query = '''SELECT DISTINCT * FROM demographic_data;'''

    res = None
    with con.cursor() as curs:
        curs.execute(query)
        res = curs.fetchall()

    for i in res:
        prepared = prepare_data(i)

        if prepared:
            fill_districts = '''INSERT INTO dim_district (district_name, region, inhabitants_cnt, municipality_cnt_type_one, municipality_cnt_type_two, municipality_cnt_type_three, municipality_cnt_type_four, cities_cnt, urban_inhabitants_ratio, avg_salary, unemploymant_rate_type_one, unemploymant_rate_type_two, enterpreneurs_cnt, crimes_cnt_type_one, crimes_cnt_type_two) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14});'''.format(prepared[1], prepared[2], prepared[3], prepared[4], prepared[5], prepared[6], prepared[7], prepared[8], prepared[9], prepared[10], prepared[11], prepared[12], prepared[13], prepared[14], prepared[15])

            with con_dw.cursor() as curs:
                curs.execute(fill_districts)
                con_dw.commit()

def fill_fact_orders(con, con_dw):
    query = '''SELECT creation_date, frequency FROM accounts GROUP BY creation_date, frequency;'''

    res = None
    with con.cursor() as curs:
        curs.execute(query)
        res = curs.fetchall()

    for i in res:
        prepared = prepare_data(i)

        if prepared:
            fill_acc_info = '''INSERT INTO dim_account (creation_date, frequency) VALUES ({0}, {1});'''.format(prepared[0], prepared[1])

            with con_dw.cursor() as curs:
                curs.execute(fill_acc_info)
                con_dw.commit()

if __name__ == '__main__':
    initial_db = 'dw-initial-db'
    con_obj_initial_db = Connection(initial_db)

    dw = 'data-warehouse'
    con_obj_dw = Connection(dw)

    con_initial_db = con_obj_initial_db.connect()
    con_dw = con_obj_dw.connect()

    fill_dim_order_type(con_initial_db, con_dw)
    fill_dim_order(con_initial_db, con_dw)
    fill_dim_account(con_initial_db, con_dw)
    fill_dim_year(con_initial_db, con_dw)
    fill_dim_month(con_initial_db, con_dw)
    fill_dim_date(con_initial_db, con_dw)
    fill_dim_district(con_initial_db, con_dw)

    con_initial_db.close()
    con_dw.close()
