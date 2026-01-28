CREATE OR REPLACE VIEW sms.customer_last_two_orders AS
SELECT
  DISTINCT
  c.customercode,
  o.invoicedate,
  DENSE_RANK() OVER (
    PARTITION BY c.customercode
    ORDER BY o.invoicedate DESC
  ) AS rn
FROM sms.sales_orders o
JOIN sms.customers c
  ON o.customerkey = c.customerkey;
