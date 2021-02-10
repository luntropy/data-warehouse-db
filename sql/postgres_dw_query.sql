CREATE TABLE IF NOT EXISTS dim_order (
    order_id SERIAL PRIMARY KEY,
    bank_to VARCHAR(255),
    account_to VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_order_type (
    order_type_id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_credit_card (
    card_id SERIAL PRIMARY KEY,
    issue_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dim_card_type (
    card_type_id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_calendar_year (
    year_id SERIAL PRIMARY KEY,
    year INT
);

CREATE TABLE IF NOT EXISTS dim_calendar_month (
    month_id SERIAL PRIMARY KEY,
    month_number INT,
    month_name VARCHAR(255),
    year_id INT,
    year INT,
    FOREIGN KEY (year_id)
        REFERENCES dim_calendar_year (year_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS dim_calendar_date (
    date_id SERIAL PRIMARY KEY,
    calendar_date DATE,
    day_number INT,
    day_of_week_name VARCHAR(255),
    month_id INT,
    month_number INT,
    month_name VARCHAR(255),
    year_id INT,
    year INT,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE,
    FOREIGN KEY (year_id)
        REFERENCES dim_calendar_year (year_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS dim_account (
    account_id SERIAL PRIMARY KEY,
    creation_date DATE,
    frequency VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dim_district (
	district_id SERIAL PRIMARY KEY,
    district_name VARCHAR(255),
    region VARCHAR(255),
    inhabitants_cnt INT,
    municipality_cnt_type_one INT,
    municipality_cnt_type_two INT,
    municipality_cnt_type_three INT,
    municipality_cnt_type_four INT,
    cities_cnt INT,
    urban_inhabitants_ratio DECIMAL,
    avg_salary DECIMAL,
    unemploymant_rate_type_one DECIMAL,
    unemploymant_rate_type_two DECIMAL,
    enterpreneurs_cnt INT,
    crimes_cnt_type_one INT,
    crimes_cnt_type_two INT
);

CREATE TABLE IF NOT EXISTS dim_client (
    client_id SERIAL PRIMARY KEY,
    birth_number DATE,
    gender CHAR
);

CREATE TABLE IF NOT EXISTS dim_disp_type (
    disp_type_id SERIAL PRIMARY KEY,
    disp_type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_transactions (
    trans_id SERIAL PRIMARY KEY,
    trans_date DATE,
    bank_to VARCHAR(255),
    account_to VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_trans_characterization (
    trans_char_id SERIAL PRIMARY KEY,
    characterization VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_trans_type (
    trans_type_id SERIAL PRIMARY KEY,
    trans_type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_trans_operation (
    trans_operation_id SERIAL PRIMARY KEY,
    operation VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dim_loan (
    loan_id SERIAL PRIMARY KEY,
    loan_date DATE
);

CREATE TABLE IF NOT EXISTS dim_loan_status (
    loan_status_id SERIAL PRIMARY KEY,
    status VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS fact_orders (
    fact_id SERIAL PRIMARY KEY,
    order_id INT,
    account_id INT,
    order_type_id INT,
    district_id INT,
    date_id INT,
    amount DECIMAL,
    FOREIGN KEY (order_id)
        REFERENCES dim_order (order_id)
        ON DELETE CASCADE,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (order_type_id)
        REFERENCES dim_order_type (order_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (date_id)
        REFERENCES dim_calendar_date (date_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_credit_cards (
    fact_id SERIAL PRIMARY KEY,
    card_id INT,
    card_type_id INT,
    client_id INT,
    account_id INT,
    disp_type_id INT,
    district_id INT,
    date_id INT,
    FOREIGN KEY (card_id)
        REFERENCES dim_credit_card (card_id)
        ON DELETE CASCADE,
    FOREIGN KEY (card_type_id)
        REFERENCES dim_card_type (card_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (client_id)
        REFERENCES dim_client (client_id)
        ON DELETE CASCADE,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (disp_type_id)
        REFERENCES dim_disp_type (disp_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (date_id)
        REFERENCES dim_calendar_date (date_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_dispositions (
    fact_id SERIAL PRIMARY KEY,
    client_id INT,
    account_id INT,
    disp_type_id INT,
    district_id INT,
    date_id INT,
    FOREIGN KEY (client_id)
        REFERENCES dim_client (client_id)
        ON DELETE CASCADE,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (disp_type_id)
        REFERENCES dim_disp_type (disp_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (date_id)
        REFERENCES dim_calendar_date (date_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    fact_id SERIAL PRIMARY KEY,
    account_id INT,
    trans_type_id INT,
    trans_operation_id INT,
    trans_char_id INT,
    district_id INT,
    date_id INT,
    amount DECIMAL,
    post_trans_account_balance DECIMAL,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (trans_type_id)
        REFERENCES dim_trans_type (trans_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (trans_operation_id)
        REFERENCES dim_trans_operation (trans_operation_id)
        ON DELETE CASCADE,
    FOREIGN KEY (trans_char_id)
        REFERENCES dim_trans_characterization (trans_char_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (date_id)
        REFERENCES dim_calendar_date (date_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_loans (
    fact_id SERIAL PRIMARY KEY,
    loan_status_id INT,
    loan_id INT,
    account_id INT,
    district_id INT,
    date_id INT,
    amount DECIMAL,
    duration INT,
    payments DECIMAL,
    FOREIGN KEY (loan_status_id)
        REFERENCES dim_loan_status (loan_status_id)
        ON DELETE CASCADE,
    FOREIGN KEY (loan_id)
        REFERENCES dim_loan (loan_id)
        ON DELETE CASCADE,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (date_id)
        REFERENCES dim_calendar_date (date_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_orders_per_type_and_account (
    fact_id SERIAL PRIMARY KEY,
    account_id INT,
    order_type_id INT,
    month_id INT,
    number_of_orders INT,
    total_amount DECIMAL,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (order_type_id)
        REFERENCES dim_order_type (order_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_eligible_for_loan (
    fact_id SERIAL PRIMARY KEY,
    month_id INT,
    number_of_accounts INT,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_cards_issued_per_type (
    fact_id SERIAL PRIMARY KEY,
    card_type_id INT,
    month_id INT,
    number_of_cards INT,
    FOREIGN KEY (card_type_id)
        REFERENCES dim_card_type (card_type_id)
        ON DELETE CASCADE,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_transactions_per_account (
    fact_id SERIAL PRIMARY KEY,
    account_id INT,
    month_id INT,
    number_deposits INT,
    number_withdraws INT,
    num_credit_cards_withdraws INT,
    num_deposits_cash INT,
    num_collections_another_bank INT,
    num_withdraws_cash INT,
    num_remittances_another_bank INT,
    amount_in_all_trans DECIMAL,
    amount_out_all_trans DECIMAL,
    num_insurance_payments INT,
    num_statement_payments INT,
    num_interests_credited INT,
    num_sanctions_negative_balance INT,
    num_household_trans INT,
    num_pension_trans INT,
    num_loan_payments INT,
    num_banks_in_trans INT,
    num_accounts_in_trans INT,
    FOREIGN KEY (account_id)
        REFERENCES dim_account (account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_districts (
    fact_id SERIAL PRIMARY KEY,
    month_id INT,
    district_id INT,
    num_clients INT,
    num_accounts INT,
    num_trans INT,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fact_granted_loans (
    fact_id SERIAL PRIMARY KEY,
    month_id INT,
    district_id INT,
    loan_status_id INT,
    amount DECIMAL,
    FOREIGN KEY (month_id)
        REFERENCES dim_calendar_month (month_id)
        ON DELETE CASCADE,
    FOREIGN KEY (district_id)
        REFERENCES dim_district (district_id)
        ON DELETE CASCADE,
    FOREIGN KEY (loan_status_id)
        REFERENCES dim_loan_status (loan_status_id)
        ON DELETE CASCADE
);
