import sys
import pandas as pd
import numpy as np
import re 
from sqlalchemy import create_engine
def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on="id")
    return(df)


def clean_data(df):
    # Expand category data 
    categories_expanded = df["categories"].str.split(pat=";", n=-1, expand=True)
    #clean the columns and rows 
    #Using the first row to make the column names
    row1=categories_expanded.head(1)    
    category_colnames = []
    for i in range(0,len(row1.columns)):
     category_colnames.append(row1[i].item())
    categories_expanded.columns = category_colnames
    #clean the rows now 
    for column in categories_expanded:
     categories_expanded[column]=categories_expanded[column].apply(lambda x: re.sub('\D', '', str(x)))
    #removing the numbers from the columns
    pattern = r'[0-9]'
    columns=categories_expanded.columns
    new_column=[]
    for item in columns:
     new_item=(re.sub("-", '', item))
     item=(re.sub(pattern, '', new_item)) 
     new_column.append(item)
    #changing the column name 
    categories_expanded.columns=new_column
    # drop the categories column from df
    
    df.drop('categories', inplace=True, axis=1)

    #merge with the main dataset df
    df=df.join(categories_expanded)
    
    return (df)

#function to save the data to the database
def save_data(df, database_filename):
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Messages', engine, index=False, if_exists='replace')



def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
    
    