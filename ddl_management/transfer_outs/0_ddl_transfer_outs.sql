use schema transfers

create or replace table transfer_outs (
    id VARCHAR(16777216),
    account_id VARCHAR(16777216),
    amount float,
    transfer_requested_at VARCHAR(16777216),
    transfer_completed_at VARCHAR(16777216),
    status VARCHAR(128)
)