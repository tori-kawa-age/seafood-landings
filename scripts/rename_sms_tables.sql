-- Friendly names for interview/demo (views)
CREATE SCHEMA IF NOT EXISTS sms;

CREATE OR REPLACE VIEW sms.customers AS
SELECT * FROM raw_sms.ar_customers;

CREATE OR REPLACE VIEW sms.sales_orders AS
SELECT * FROM raw_sms.oe_orders;

CREATE OR REPLACE VIEW sms.sales_order_lines AS
SELECT * FROM raw_sms.oe_orderlines;

-- Optional product reference tables
CREATE OR REPLACE VIEW sms.product_categories AS
SELECT * FROM raw_sms.ic_codeproductcategories;

CREATE OR REPLACE VIEW sms.product_classifications AS
SELECT * FROM raw_sms.ic_codeproductclassifications;

