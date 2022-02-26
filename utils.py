from datetime import date, timedelta, datetime

import pandas as pd


def fetch_transaction_info(transaction_id):        
    col_list = ["transaction_id", "sku_id", "sku_price", "transaction_datetime"]

    # Convert the csv data filtered by transaction_id into pandas dataframe    
    df = (pd.read_csv("data/transaction.csv", nrows=1, usecols=col_list)
        [lambda x : x['transaction_id'] == int(transaction_id)])
    
    # Convert the sku csv data into pandas dataframe    
    sku_df = pd.read_csv("data/sku.csv", usecols=["sku_id", "sku_name"])

    # Merge both dataframes where sku_id is same    
    df = pd.merge(df, sku_df, on='sku_id')    

    # Drop unnecessary columns from final result
    df = df.drop(['sku_id'], axis=1)
    
    data = df.to_dict('records')
    
    if len(data) >= 1 :        
        # Convert the datetime object into proper format of dd/mm/yyyy
        datetime_obj = datetime.strptime(data[0]['transaction_datetime'], '%Y-%m-%d %H:%M:%S')        
        data[0]['transaction_datetime'] = datetime_obj.strftime("%d/%m/%Y")
        return data[0]
    return dict()


def fetch_transaction_summary(no_of_days, field_name):
    last_date = date.today() - timedelta(days=int(no_of_days))

    col_list = ["sku_id", "sku_price", "transaction_datetime"]
    
    df = (pd.read_csv("data/transaction.csv", usecols=col_list)
      [lambda x: x['transaction_datetime'] >= str(last_date)])
    
    sku_df = pd.read_csv("data/sku.csv", usecols=["sku_id", field_name])
    
    df = pd.merge(df, sku_df, on='sku_id')
    df = df.groupby([field_name], as_index=False).sum()        
    df = df.drop(['sku_id'], axis=1)
    df.rename(columns = {"sku_price": "total_amount"}, 
          inplace = True)
    final_data = df.to_dict('records')
    
    return final_data
