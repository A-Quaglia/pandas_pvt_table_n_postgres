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

## How to Run the Project
To run this project locally, follow these steps:
### 1. Clone the Repository
First, clone the repository to your local machine:
```
git clone https://github.com/A-Quaglia/pandas_pvt_table_n_postgres.git
cd pandas_pvt_table_n_postgres
```

### 2. Install Project Dependencies
If you haven't already installed Poetry, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).
Once Poetry is installed, use it to install the project's dependencies:
```
poetry install
```

### 3. Configure Database Connection
Ensure that your local PostgreSQL database is set up and the [Northwind database is configured](https://github.com/pthom/northwind_psql). You should update the connection settings in the .env file with your database credentials - first delete `.template` from the file extension.

### 4. Run the Jupyter Notebook
To run the Jupyter Notebook and execute the analysis:
```
poetry shell
```
Start Jupyter Notebook:
```
jupyter notebook
```
Open and run the `northwind_analysis.ipynb` notebook to reproduce the study and results.