-- dbt/models/staging/stg_customers.sql
select
  trim(customerkey)     as customerkey,
  trim(customercode)    as customercode,
  name          as name
from {{ source('sms', 'customers') }}
