-- models/marts/fct_customer_last_two_orders.sql

select
  customercode,
  invoicedate,
  order_rank
from {{ ref('int_cust_recent_orders') }}
where order_rank <= 2
