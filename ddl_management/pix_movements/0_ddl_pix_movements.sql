use schema pix

create or replace table pix_movements (
    transaction_id VARCHAR(16777216),
    account_id VARCHAR(16777216),
    type VARCHAR(128),
    amount float,
    investment_requested_at VARCHAR(16777216),
    investment_completed_at VARCHAR(16777216),
    status VARCHAR(128)
)