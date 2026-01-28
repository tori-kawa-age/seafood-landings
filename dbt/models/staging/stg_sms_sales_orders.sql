-- dbt/models/staging/stg_sales_orders.sql
select
  trim(customerkey)                          as customerkey,
  cast(invoicedate as timestamp)             as invoicedate,
  so.ordernumber                                as ordernumber,
  cast(invoicesubtotal as numeric)           as invoicesubtotal,
  cast(totalweight as numeric)               as totalweight,
  trim(sol.productkey)                           as productkey
from {{ source('sms', 'sales_orders') }} so
join {{ source('sms', 'sales_order_lines')}} sol
  on so.ordernumber = sol.ordernumber
