use schema locations

create or replace table states (
    state_id VARCHAR(16777216),
    state VARCHAR(256),
    country_id VARCHAR(16777216)
)