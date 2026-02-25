# Python and SQL training

## Starters
### Define these SQL concepts:

- ### Granularity  

    Is an atribute of a Sql table, it represents the ammount of information each entry on that table can possess (how many collumns each rows has), it can be define from low to high granularity, where low would be fewer information (collumns) that any entry (row) has. Lower granularity means faster processing.  
    
- ### Attributes/Measures/Constants  

    These are types of values a query can use.
    ATTRIBUTES are the raw data that you want from a table, where you don't make meaninful manipulation of the value. Ex.: Product name, product price.  

    MEASURES would be manipulated data from the table. Ex.: The total sum of sales in a month, the biggest sale by value made in a day.  

    CONSTANTS are fixed values defined in the query. Ex.: 0.10 as productivity_bonus.

- ### Star Schema  

    It's a design pattern for databases where you have a central table (aka fact table) and surrounding tables (aka dimension tables). It's used especially for data warehouses. The fact table contains the main data and get suplementary data from the surrounding ones.  
    It reminded me of Object-Oriented Programming in principle.

- ### The OLAP cube  

    Online Analytical Processing is framework for analytical data processing mostly used for BI and the OLAP Cube is a data structure used in it.
    Where a table is a 2D representation the OLAP Cube brings depth, adding a third element to the analisys.  
    Ex.: An analisys of sales of a certain item in a certain group of places (Table - 2D), add a periodicity to the analisys and you get the Cube.  
    
## Pratical example - Store Sales

Suppose we have to keep track of the sales across multiple stores. Those stores share multiple
products. And each store has a bunch of sales every day. You have one huge table
with the following columns:

Date, Value, ProductId, ProductName, StoreId, StoreName, Category, Subcategory, 
State, Street, Country;

### Theoretical Questions:

- ### Which are the columns that have the biggest variance across the data?  

    Assuming that Date will bring year-month-day (and not time like DATETIME or TIMESTAMP would), i believe that value, productId, productName, storeId, storeName, Date, Street are the ones that will have the highest variance, category and subcategory tend to have less and City (missing in the question, added cause it makes sense), State and Country most likely are the ones with less variance.  

    But as with almost everything, it uncertain, if we look just a couple of days than Date will have less variance, if there is thousands of stores it can change the order, maybe it's a franchise that will only have one store per city and they try their best to be at 'Main Street', than street can be one of the attributes with least variance.

- ### What is the difference of storing a column that varies in comparison to one that is constant most of the time?  

    When you have less variation the data can be compressed since the DB (if the DB handles compression) can store the value once and then refer to it in all other instances.  
    For processing the data using Parquet (or some other Columnar Storage) low variance is compressed so storaging space required is reduced and this also makes the data analysis faster (unless some very specific cases where the amount of data is already tiny, the act of compressing and decompressing may end up taking more time than the actual analysis)

- ### How could we optimize the storage?  

    The best way would be to use a Star Schema where the Fact table would hold only Id for info that would be placed in a couple of Dimension table linking the by the XXX_Id (ex.: One table for the Store, and other for Product, maybe even one for the Category/Subcategory).
    We could also look to remove data that is constant, like Country if there is no international stores.  
    And at last look to storage it in columnar storage and enable compression.
