import duckdb


# Lesson 01 - Create an optimized structure for that storage! We have a big table stored as a CSV in`python_sql_training/lesson_01/resources/big.parquet`.  

## Step 01: Read the file to understand the data in it.
def readTableColumns():
    '''
    Gets columns information and print it.
    '''
    # print(duckdb.read_parquet('resources/big.parquet'))
    print('Columns Information from big.parquet')
    print(duckdb
          .sql(
              '''
              DESCRIBE SELECT * FROM 'resources/big.parquet'
              '''))

#### At first i decided to try using duckdb.read_parquet function, and print the result, but i found out that the  table had to many collumns to be displayed in my VSCode terminal window. So after checking the documentation i decided to try and use a SQL statement and got what i wanted.  

#### Date (date); Value (double); ProductId (BigInt); ProductName (varchar); StoreId (BigInt); StoreName (varchar); Category (varchar); Subcategory (varchar); State (varchar); Street (varchar); Country (varchar).  

#### With that information, the way to optimize structure for that storage is extract it with a Star Schema approach.


## Step 02: Extract data from big.parquet to create new specified tables. 

def createNewTables():
    '''
    Extract data from big table to three new table sales, products and stores and print a sample of it
    '''
    duckdb.sql(
        '''
        SELECT DISTINCT Date, Value, ProductId, StoreId FROM 
        read_parquet('resources/big.parquet') 
        ORDER BY Date desc
        '''
    ).write_parquet('resources/sales.parquet')

    print('Sales Table')
    print(duckdb.sql(
              '''
              SELECT * FROM 'resources/sales.parquet' LIMIT 10
              '''))

    duckdb.sql(
            '''
            SELECT DISTINCT ProductId, ProductName, Category, Subcategory
            FROM read_parquet('resources/big.parquet') 
            ORDER BY ProductId
            '''
    ).write_parquet('resources/products.parquet')

    print('Products Table')
    print(duckdb.sql(
              '''
              SELECT * FROM 'resources/products.parquet' LIMIT 10
              '''))

    duckdb.sql(
        '''
        SELECT DISTINCT StoreId, StoreName, State, Street, Country 
        FROM read_parquet('resources/big.parquet')
        ORDER BY StoreId
        '''
    ).write_parquet('resources/stores.parquet')

    print('Stores Table')
    print(duckdb.sql(
              '''
              SELECT * FROM 'resources/stores.parquet' LIMIT 10
              '''))


# Lesson 02 - Which are the total sales by store? Which are the total sales by product?

## Using the tables generated on the last challenge

def extractSalesByStore():

    duckdb.sql(
        '''
        SELECT StoreName, ROUND(SUM(Value), 2) as TotalSales
        FROM read_parquet('resources/sales.parquet') sales
        LEFT JOIN read_parquet('resources/stores.parquet') store
            ON sales.StoreId = store.StoreId
        GROUP BY StoreName
        ORDER BY TotalSales desc
        '''        
    ).write_parquet('resources/sales_by_stores.parquet')

    print('Sales By Store Table')
    print(duckdb
          .sql(
              '''
              SELECT * FROM 'resources/sales_by_stores.parquet'
              '''))

def extractSalesByProduct():

    duckdb.sql(
        '''
        SELECT ProductName, ROUND(SUM(Value), 2) as TotalSales
        FROM read_parquet('resources/sales.parquet') sales
        LEFT JOIN read_parquet('resources/products.parquet') product
            ON sales.ProductId = product.ProductId
        GROUP BY ProductName
        ORDER BY TotalSales desc
        '''   
    ).write_parquet('resources/sales_by_product.parquet')

    print('Sales by Product Table')
    print(duckdb
          .sql(
              '''
              SELECT * FROM 'resources/sales_by_product.parquet'
              '''))

# Lesson 03 - Which is the total share by store?

def extractSharesByStore():
    print('Store Share')
    duckdb.query(
        '''
        SELECT 
            sales.StoreName, 
            sales.TotalSales as StoreSales, 
            ROUND(sales.TotalSales/(SUM(sales.TotalSales) OVER())*100 , 2) as StoreShare
        FROM read_parquet('resources/sales_by_stores.parquet') sales
        ORDER BY StoreShare desc
        '''
    ).show()


def main():
        # Lesson 01
    readTableColumns()
    createNewTables()
        #Lesson 02
    extractSalesByStore()
    extractSalesByProduct()
        #Lesson 03
    extractSharesByStore()

if __name__ == "__main__":
    main()




