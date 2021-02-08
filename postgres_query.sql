CREATE TABLE IF NOT EXISTS demographic_data (
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

CREATE TABLE IF NOT EXISTS accounts (
	account_id SERIAL PRIMARY KEY,
    district_id INT,
    creation_date DATE,
    frequency VARCHAR(20),
    FOREIGN KEY (district_id)
		REFERENCES demographic_data (district_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS clients (
	client_id SERIAL PRIMARY KEY,
    district_id INT,
    birth_number DATE,
    gender CHAR,
	FOREIGN KEY (district_id)
		REFERENCES demographic_data (district_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS disposition (
	disp_id SERIAL PRIMARY KEY,
    client_id INT,
    account_id INT,
    disp_type VARCHAR(255),
    FOREIGN KEY (client_id)
		REFERENCES clients (client_id)
		ON DELETE CASCADE,
	FOREIGN KEY (account_id)
		REFERENCES accounts (account_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS permanent_order (
	order_id SERIAL PRIMARY KEY,
    account_id INT,
    bank_to VARCHAR(255),
    account_to VARCHAR(255),
    amount DECIMAL,
    k_symbol VARCHAR(255),
    FOREIGN KEY (account_id)
		REFERENCES accounts (account_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS transactions (
	trans_id SERIAL PRIMARY KEY,
    account_id INT,
    trans_date DATE,
    trans_type VARCHAR(255),
    operation VARCHAR(255),
    amount DECIMAL,
    balance DECIMAL,
    k_symbol VARCHAR(255),
    bank VARCHAR(255),
    partner_account VARCHAR(255),
    FOREIGN KEY (account_id)
		REFERENCES accounts (account_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS loans (
	loan_id SERIAL PRIMARY KEY,
    account_id INT,
    loan_date DATE,
    amount DECIMAL,
    duration INT,
    payments DECIMAL,
    loan_status CHAR,
    FOREIGN KEY (account_id)
		REFERENCES accounts (account_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS credit_cards (
	card_id SERIAL PRIMARY KEY,
    disp_id INT,
    card_type VARCHAR(255),
    issued TIMESTAMP,
    FOREIGN KEY (disp_id)
		REFERENCES disposition (disp_id)
		ON DELETE CASCADE
);
