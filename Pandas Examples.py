#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data Input/Output
#     pd.read_csv() : Reads a CSV file into a Pandas dataframe
#     pd.read_excel() : Reads an Excel file into a Pandas dataframe
#     pd.read_sql() : Reads data from a SQL database into a Pandas dataframe
#     df.to_csv() : Writes a Pandas dataframe to a CSV file
#     df.to_excel() : Writes a Pandas dataframe to an Excel file
#     df.to_sql() : Writes a Pandas dataframe to a SQL database

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Math': [80, 90, 70, 85, 95],
    'Science': [85, 95, 75, 90, 80],
    'English': [90, 80, 85, 95, 75]
}

df = pd.DataFrame(data)
print(df)

# Reading data from a CSV file
df_csv = pd.read_csv('students.csv')
print(df_csv)

# Writing data to a CSV file
df.to_csv('students.csv', index=False)

# Reading data from an Excel file
df_excel = pd.read_excel('students.xlsx', sheet_name='Sheet1')
print(df_excel)

# Writing data to an Excel file
df.to_excel('students.xlsx', sheet_name='Sheet1', index=False)

# Establishing a connection to a SQLite database
import sqlite3
conn = sqlite3.connect('students.db')

# Reading data from a SQL table
df_sql = pd.read_sql('SELECT * FROM students', conn)
print(df_sql)

# Writing data to a SQL database
df.to_sql('students', conn, if_exists='replace', index=False)

# Closing the connection
conn.close()


# In[1]:


# Data Manipulation
#     df.head() : Returns the first n rows of the dataframe (default n=5)
#     df.tail() : Returns the last n rows of the dataframe (default n=5)
#     df.shape : Returns the dimensions of the dataframe (rows, columns)
#     df.columns : Returns the column labels of the dataframe
#     df.describe() : Computes summary statistics of the dataframe
#     df.info() : Provides information about the dataframe, such as column data types and missing values
#     df.isnull() : Returns a boolean dataframe indicating which values are missing (NaN)
#     df.dropna() : Removes rows or columns containing missing values
#     df.fillna() : Fills missing values with a specified value or method (e.g., forward fill or backward fill)
#     df.groupby() : Groups the dataframe by one or more columns and applies an aggregation function (e.g., sum, mean, count)
#     df.merge() : Combines two dataframes based on a common column(s)
#     df.sort_values() : Sorts the dataframe by one or more columns
#     df.pivot() : Creates a pivot table from the dataframe

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Math': [80, 90, 70, 85, 95],
    'Science': [85, 95, 75, 90, 80],
    'English': [90, 80, 85, 95, 75]
}

df = pd.DataFrame(data)
print(df)

# Returns the first n rows of the dataframe (default n=5)
print(df.head())

# Returns the last n rows of the dataframe (default n=5)
print(df.tail())

# Returns the dimensions of the dataframe (rows, columns)
print(df.shape)

# Returns the column labels of the dataframe
print(df.columns)

# Computes summary statistics of the dataframe
print(df.describe())

# Provides information about the dataframe, such as column data types and missing values
print(df.info())

# Returns a boolean dataframe indicating which values are missing (NaN)
print(df.isnull())

# Removes rows or columns containing missing values
print(df.dropna())

# Fills missing values with a specified value or method (e.g., forward fill or backward fill)
print(df.fillna(method='ffill'))

# Groups the dataframe by one or more columns and applies an aggregation function (e.g., sum, mean, count)
print(df.groupby('Age').sum())

# Combines two dataframes based on a common column(s)
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Gender': ['F', 'M', 'M', 'M', 'F']
}
df2 = pd.DataFrame(data2)

print(df.merge(df2, on='Name'))

# Sorts the dataframe by one or more columns
print(df.sort_values('Math'))

# Creates a pivot table from the dataframe
print(df.pivot(index='Name', columns='Age', values='Math'))


# Manipulating two or more columns

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Math': [80, 90, 70, 85, 95],
    'Science': [85, 95, 75, 90, 80],
    'English': [90, 80, 85, 95, 75]
}

df = pd.DataFrame(data)
print(df)

# Returns the first n rows of the dataframe (default n=5) using two columns
print(df[['Name', 'Math']].head())

# Returns the last n rows of the dataframe (default n=5) using two columns
print(df[['Science', 'English']].tail())

# Returns the dimensions of the dataframe (rows, columns) using two columns
print(df[['Name', 'Age', 'English']].shape)

# Returns the column labels of the dataframe using two columns
print(df[['Math', 'Science']].columns)

# Computes summary statistics of the dataframe using two columns
print(df[['Age', 'Science']].describe())

# Provides information about the dataframe, such as column data types and missing values using two columns
print(df[['Name', 'Math']].info())

# Returns a boolean dataframe indicating which values are missing (NaN) using two columns
print(df[['Age', 'English']].isnull())

# Removes rows or columns containing missing values using two columns
print(df[['Math', 'Science']].dropna())

# Fills missing values with a specified value or method (e.g., forward fill or backward fill) using two columns
print(df[['Science', 'English']].fillna(method='ffill'))

# Groups the dataframe by one or more columns and applies an aggregation function (e.g., sum, mean, count) using two columns
print(df.groupby(['Age', 'Name'])[['Math', 'Science']].mean())

# Combines two dataframes based on a common column(s) using two columns
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Gender': ['F', 'M', 'M', 'M', 'F']
}
df2 = pd.DataFrame(data2)

print(df[['Name', 'Math']].merge(df2, on='Name'))

# Sorts the dataframe by one or more columns using two columns
print(df[['Name', 'Science']].sort_values(['Science', 'Name']))

# Creates a pivot table from the dataframe using two columns
print(df.pivot(index='Name', columns='Age', values=['Math', 'Science']))


# In[3]:


# Data Selection
#     df.loc[] : Selects rows and columns by label
#     df.iloc[] : Selects rows and columns by integer location
#     df[] : Selects columns by label
#     df[col] : Selects a single column by label
#     df.ix[] : Selects rows and columns by label or integer location (deprecated, use .loc[] or .iloc[] instead)
#     df.at[] : Selects a single value by label
#     df.iat[] : Selects a single value by integer location
#     df.query() : Selects rows based on a boolean condition

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Math': [80, 90, 70, 85, 95],
    'Science': [85, 95, 75, 90, 80],
    'English': [90, 80, 85, 95, 75]
}

df = pd.DataFrame(data)
print(df)

# Selects rows and columns by label using two columns
print(df.loc[[1,3], ['Name', 'Math']])

# Selects rows and columns by integer location using two columns
print(df.iloc[[1,3], [0,2]])

# Selects columns by label using one column
print(df[['Name']])

# Selects a single column by label using one column
print(df['Math'])


# Selects a single value by label using one column
print(df.at[3, 'Science'])

# Selects a single value by integer location using one column
print(df.iat[2, 4])

# Selects rows based on a boolean condition using one column
print(df[df['Age'] > 30])


# In[4]:


# Data Cleaning
#     df.drop_duplicates() : Removes duplicate rows from the dataframe
#     df.replace() : Replaces specified values in the dataframe with another value
#     df.rename() : Renames columns or rows in the dataframe
#     df.astype() : Changes the data type of one or more columns in the dataframe
#     df.apply() : Applies a function to each element, row or column of the dataframe
#     df.duplicated() : Returns a boolean dataframe indicating which rows are duplicates of previous rows
#     df.str() : Provides string methods for columns with string data type

import pandas as pd

# Creating a sample dataset with duplicates
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Alice'],
    'Age': [25, 30, 35, 40, 45, 25],
    'Math': [80, 90, 70, 85, 95, 80],
    'Science': [85, 95, 75, 90, 80, 85],
    'English': [90, 80, 85, 95, 75, 90]
}

df = pd.DataFrame(data)
print(df)

# Removes duplicate rows from the dataframe
print(df.drop_duplicates())

# Replaces specified values in the dataframe with another value
print(df.replace({'Alice': 'A', 80: 85}))

# Renames columns or rows in the dataframe
print(df.rename(columns={'Math': 'Mathematics', 'Age': 'Years'}))

# Changes the data type of one or more columns in the dataframe
df['Age'] = df['Age'].astype(float)
print(df.dtypes)

# Applies a function to each element, row or column of the dataframe
print(df.apply(lambda x: x * 2))

# Returns a boolean dataframe indicating which rows are duplicates of previous rows
print(df.duplicated())

# Provides string methods for columns with string data type
df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
                    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'emily@example.com']})
print(df2['Email'].str.upper())


# In[ ]:




