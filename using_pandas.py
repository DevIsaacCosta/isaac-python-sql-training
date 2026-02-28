import pandas as pd


def read_big_table():
    return pd.read_parquet('resources/big.parquet')

big_table = read_big_table()

def get_table_info():
    print(big_table.info())

def print_table_sample():
    print(big_table.head())
    print(big_table.tail())

def save_parquet_with_pandas():
    big_table.to_parquet('resources/big_pandas.parquet')


big_table_pandas = pd.read_parquet('resources/big_pandas.parquet')

def create_sales_table():
    return big_table_pandas[['Date', 'Value', 'ProductId', 'StoreId']]

def create_products_table():
    return big_table_pandas[['ProductId', 'ProductName', 'Category', 'Subcategory']].drop_duplicates()

def create_stores_table():
    return big_table_pandas[['StoreId', 'StoreName', 'State', 'Street', 'Country']].drop_duplicates()

def create_new_tables_parquet_with_pandas():
    create_sales_table().to_parquet('resources/fact_sales_pandas.parquet')
    create_products_table().to_parquet('resources/dim_products_pandas.parquet')
    create_stores_table().to_parquet('resources/dim_stores_pandas.parquet')

#print(pd.read_parquet('resources/fact_sales_pandas.parquet'))

#print(pd.read_parquet('resources/dim_products_pandas.parquet'))

#print(pd.read_parquet('resources/dim_stores_pandas.parquet'))

def extract_sales_by_store():
    # return big_table_pandas.groupby(['StoreId', 'StoreName'])['Value'].sum()
    return big_table_pandas.groupby(['StoreId', 'StoreName']).aggregate({'Value' :'sum'}).rename(columns={'Value' : 'TotalSales'})

# print(extract_sales_by_store())

def extract_sales_by_product():
    return big_table_pandas[['ProductId', 'ProductName', 'Category', 'Subcategory', 'Value']].groupby(['ProductId','ProductName', 'Category', 'Subcategory']).aggregate({'Value' :'sum'})

# print(extract_sales_by_product())

def extract_share_by_store():
    return big_table_pandas[['StoreId', 'StoreName', 'Value']].groupby(['StoreId', 'StoreName']).aggregate({'Value' :'sum'}).assign(TotalSales = lambda x : x['Value'].sum(), StoreShare = lambda y : y['Value'] / y['TotalSales'] * 100)

# print(extract_share_by_store())