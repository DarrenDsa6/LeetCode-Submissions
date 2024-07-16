Select Product.product_name, year, price from Sales
Join Product
ON Sales.product_id = Product.product_id;
