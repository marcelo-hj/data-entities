use schema dates

create or replace table d_time (
    time_id VARCHAR(16777216),
    action_timestamp TIMESTAMP_TZ,
    week_id VARCHAR(16777216),
    month_id VARCHAR(16777216),
    year_id VARCHAR(16777216),
    weekday_id VARCHAR(16777216)
)