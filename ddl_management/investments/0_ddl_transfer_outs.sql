use schema investments;

create or replace table investments (
    transaction_id VARCHAR(16777216),
    account_id VARCHAR(16777216),
    type VARCHAR(128),
    amount float,
    investments_requested_at VARCHAR(16777216),
    investments_completed_at VARCHAR(16777216),
    status VARCHAR(128)
);