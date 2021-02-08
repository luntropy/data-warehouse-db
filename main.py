#!/usr/bin/python3

import csv

from modules.connection import Connection

def prepare_data(data):
    for i in range(0, len(data)):
        if data[i] == '?':
            data[i] = 'NULL'
        else:
            data[i] = "'" + data[i] + "'"

def prepare_data_client(data):
    gender = 'M'

    for i in range(0, len(data)):

        if i == 1 and data[i] != '?':
            new_date = list(data[i])
            month = data[i][2:4]

            if int(month) > 12:
                gender = 'F'
                month = str(int(month) - 50)

                if len(month) == 1:
                    month = '0' + month

                new_date[2] = month[0]
                new_date[3] = month[1]

            new_date = ''.join(new_date)
            data[i] = new_date

        if data[i] == '?':
            data[i] = 'NULL'
        else:
            data[i] = "'" + data[i] + "'"

    gender = "'" + gender + "'"
    data.append(gender)

def fill_demographic_table():
    with open('./data_berka/district.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM demographic_data;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO demographic_data (district_id, district_name, region, inhabitants_cnt, municipality_cnt_type_one, municipality_cnt_type_two, municipality_cnt_type_three, municipality_cnt_type_four, cities_cnt, urban_inhabitants_ratio, avg_salary, unemploymant_rate_type_one, unemploymant_rate_type_two, enterpreneurs_cnt, crimes_cnt_type_one, crimes_cnt_type_two) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15});'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_accounts_table():
    with open('./data_berka/account.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM accounts;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO accounts (account_id, district_id, frequency, creation_date) VALUES ({0}, {1}, {2}, {3});'''.format(row[0], row[1], row[2], row[3])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_clients_table():
    with open('./data_berka/client.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM clients;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data_client(row)

            insertion_query = '''INSERT INTO clients (client_id, birth_number, district_id, gender) VALUES ({0}, {1}, {2}, {3});'''.format(row[0], row[1], row[2], row[3])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_disposition_table():
    with open('./data_berka/disp.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM disposition;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO disposition (disp_id, client_id, account_id, disp_type) VALUES ({0}, {1}, {2}, {3});'''.format(row[0], row[1], row[2], row[3])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_permanent_order_table():
    with open('./data_berka/order.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM permanent_order;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO permanent_order (order_id, account_id, bank_to, account_to, amount, k_symbol) VALUES ({0}, {1}, {2}, {3}, {4}, {5});'''.format(row[0], row[1], row[2], row[3], row[4], row[5])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_transactions_table():
    with open('./data_berka/trans.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM transactions;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO transactions (trans_id, account_id, trans_date, trans_type, operation, amount, balance, k_symbol, bank, partner_account) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_loans_table():
    with open('./data_berka/loan.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM loans;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO loans (loan_id, account_id, loan_date, amount, duration, payments, loan_status) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6});'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

def fill_credit_cards_table():
    with open('./data_berka/card.asc', 'r') as data_file:
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        con_obj = Connection()
        con = con_obj.connect()

        check_inserted_query = '''SELECT * FROM credit_cards;'''

        rows_cnt = sum(1 for row in data)
        data_file.seek(0)
        next(data_file)
        data = csv.reader(data_file, delimiter = ';')

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('The data is already inserted.')
                con.close()

                return

        for row in data:
            prepare_data(row)

            insertion_query = '''INSERT INTO credit_cards (card_id, disp_id, card_type, issued) VALUES ({0}, {1}, {2}, {3});'''.format(row[0], row[1], row[2], row[3])

            with con.cursor() as curs:
                curs.execute(insertion_query)
                con.commit()

        with con.cursor() as curs:
            curs.execute(check_inserted_query)

            if len(curs.fetchall()) == rows_cnt:
                print('Successful data insertion.')
                data_file.seek(1)

        con.close()

if __name__ == '__main__':
    fill_demographic_table()
    fill_accounts_table()
    fill_clients_table()
    fill_disposition_table()
    fill_permanent_order_table()
    fill_transactions_table()
    fill_loans_table()
    fill_credit_cards_table()

    # credit_cards table:
    # Can separate date and time of card creation into two different columns. Right now it is in one column of type timestamp.
