CREATE TABLE users(
    id UUID UNIQUE NOT NULL,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salary FLOAT NOT NULL,
    salary_day INT NOT NULL,
    debtors TEXT NULL, 
    to_pay FLOAT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


CREATE TABLE credit_cards(
    id UUID UNIQUE NOT NULL,
    user_id UUID UNIQUE NOT NULL,
    name TEXT NOT NULL,
    due_date TEXT NOT NULL,
   	cc_limit FLOAT NULL,
    due FLOAT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);

CREATE TABLE bills(
    id UUID UNIQUE NOT NULL,
    user_id UUID NOT NULL,
    cc_id UUID NULL,
    name TEXT NOT NULL,
    value FLOAT NOT NULL,
    statements INT NOT NULL,
    actual_statement INT NOT NULL,
    statement_value FLOAT NULL,
    remaining FLOAT NULL,
    float TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (cc_id) REFERENCES credit_cards(id) ON DELETE CASCADE);
    


    