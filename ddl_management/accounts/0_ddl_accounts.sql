use schema accounts

create or replace table accounts(
    account_id VARCHAR(16777216),
    customer_id VARCHAR(16777216),
    created_at TIMESTAMP_TZ,
    status VARCHAR(16777216),
    account_branch VARCHAR(16777216),
    account_check_digit VARCHAR(16777216),
    account_number VARCHAR(16777216)
)