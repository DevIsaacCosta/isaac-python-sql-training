"""
Lesson 01 - Create an optimized structure for that storage!
Lesson 02 - Which are the total sales by store? Which are the total sales by product?
Lesson 03 - Which is the total share by store?

- CSV Stored at `python_sql_training/lesson_01/resources/big.parquet`.
"""

import duckdb


# Step 01: Read the file to understand the data in it.
def read_table_columns():
    """
    Gets columns information and print it.

    At first i decided to try using duckdb.read_parquet function, and print the result,
    but i found out that the table had to many collumns to be displayed in my VSCode
    terminal window.

    So after checking the documentation i decided to try and use a SQL statement and
    got what i wanted.

    - Date (date);
    - Value (double);
    - ProductId (BigInt);
    - ProductName (varchar);
    - StoreId (BigInt);
    - StoreName (varchar);
    - Category (varchar);
    - Subcategory (varchar);
    - State (varchar);
    - Street (varchar);
    - Country (varchar).

    With that information, the way to optimize structure for that storage is extract it with a Star Schema approach.
    """
    # print(duckdb.read_parquet('resources/big.parquet'))
    print("Column Information from big.parquet")
    duckdb.sql("""
               describe select *
               from read_parquet('resources/big.parquet')
               """).show()


def create_new_tables():
    """
    Step 02: Extract data from big.parquet to create new specified tables.

    Extract data from big table to three new table sales, products and stores and print a sample of it
    """

    duckdb.sql("""
               select distinct Date, Value, ProductId, StoreId
               from
                   read_parquet('resources/big.parquet')
               order by Date desc
               """).write_parquet("resources/sales.parquet")

    print("Sales Table")
    duckdb.sql("""
               select *
               from read_parquet('resources/sales.parquet')
               limit 10
               """).show()

    duckdb.sql("""
               select distinct ProductId, ProductName, Category, Subcategory
               from read_parquet('resources/big.parquet')
               order by ProductId
               """).write_parquet("resources/products.parquet")

    print("Products Table")
    duckdb.sql("""
               select *
               from read_parquet('resources/products.parquet')
               limit 10
               """).show()

    duckdb.sql("""
               select distinct StoreId, StoreName, State, Street, Country
               from read_parquet('resources/big.parquet')
               order by StoreId
               """).write_parquet("resources/stores.parquet")

    print("Stores Table")
    duckdb.sql("""
               select *
               from read_parquet('resources/stores.parquet')
               limit 10
               """).show()


def extract_sales_by_store():
    """
    Using the tables generated on the last challenge
    """
    duckdb.sql("""
               select StoreName,
                      sum(Value) as TotalSales
               from read_parquet('resources/sales.parquet') sales
               left join read_parquet('resources/stores.parquet') store on sales.StoreId = store.StoreId
               group by StoreName
               order by TotalSales desc
               """).write_parquet("resources/sales_by_stores.parquet")

    print("Sales By Store Table")
    duckdb.sql("""
               select *
               from read_parquet('resources/sales_by_stores.parquet')
               """).show()


def extract_sales_by_product():
    duckdb.sql("""
               select ProductName,
                      sum(Value) as TotalSales
               from read_parquet('resources/sales.parquet') sales
               left join read_parquet('resources/products.parquet') product on sales.ProductId = product.ProductId
               group by ProductName
               order by TotalSales desc
               """).write_parquet("resources/sales_by_product.parquet")

    print("Sales by Product Table")
    duckdb.sql("""
               select *
               from read_parquet('resources/sales_by_product.parquet')
               """).show()


def extract_share_by_store():
    """
    Lesson 03 - Which is the total share by store?
    """
    print("Store Share")
    duckdb.query("""
                 select sales.StoreName,
                        format('{:.2f}%', sales.TotalSales) as StoreSales,
                        format('{:.2f}%', sales.TotalSales / (sum(sales.TotalSales) over ()) * 100) as StoreShare
                 from read_parquet('resources/sales_by_stores.parquet') sales
                 order by StoreShare desc
                 """).show()

    print("Another way, using the raw tables")
    duckdb.query(
        """
        select StoreName,
               format('{:,.2f}', sum(Value)) as StoreSales,
               format('{:,.2f}', sum(sum(Value)) over ()) as TotalSales,
               format('{:.2f}%', sum(Value) / (sum(sum(Value)) over ()) * 100) as StoreShare
        from read_parquet('resources/sales.parquet') fact
        left join read_parquet('resources/stores.parquet') store on fact.StoreId = store.StoreId
        group by StoreName
        order by StoreShare desc
        """
    ).show()


def main():
    # Lesson 01
    read_table_columns()
    create_new_tables()
    # Lesson 02
    extract_sales_by_store()
    extract_sales_by_product()
    # Lesson 03
    extract_share_by_store()


if __name__ == "__main__":
    main()
