use schema accounts

create or replace table customers(
    customer_id VARCHAR(16777216),
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    created_at TIMESTAMP_TZ,
    customer_city VARCHAR(16777216),
    country_name VARCHAR(128),
    cpf int
)