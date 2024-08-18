# pandas_pvt_table_n_postgres

Pandas Pivot Table and Postgres Connection Study
This is a quick study I conducted Pandas `pivot_table` method. I'm currently studying SQL data querying and manipulation, so I proposed to connect to a local Postgres database that I'm working on to apply the Pandas `pivot_table` transformation. In this case, I've used [Northwind](https://github.com/pthom/northwind_psql) - a Microsoft sample database.

## Proposed Exercise
In summary, this ended up as an exercise to achieve:
1. [Setup up Northwind tables in Postgres](https://github.com/pthom/northwind_psql) 
2. Connect to Postgres database and read orders table as a `pandas.DataFrame`
3. Create table of orders by customers by year
4. Create a barplot of the 10 greeters customers by total orders and stack it by years
## Results
**Orders by customers by year**

![alt text](<images/Pasted image 20240818171816.png>)

**TOP 10 Customers**

![alt text](<images/Pasted image 20240818171843.png>)