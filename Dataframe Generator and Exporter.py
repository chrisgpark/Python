#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python code imports CSV files into dataframes, combines them into one dataframe, 
#     displays information about columns, prompts the user to generate dataframes or export 
#     them as CSV files, and generates monthly dataframes while exporting them if the user 
#     chooses to do so.


# In[ ]:


# Code Block 1
#     This code block imports CSV files from a specific folder and creates 
#     a dictionary of dataframes using Pandas' read_csv() method. It loops over all 
#     months and years, checking if each CSV file exists, and reads it into a dataframe 
#     if it does. It then prints the number of dataframes successfully imported into 
#     the dictionary.

import pandas as pd

# set folder path
folder_path = 'INPUT DIRECTORY HERE'

# set start and end years
start_year = 2021
end_year = 2023

# create empty dictionary to store dataframes
dfs = {}

# loop over years and months
for year in range(start_year, end_year):
    for month in range(1, 13):  # loop over all 12 months
        # create file name using f-strings
        file_name = f'resi_data_{year}_{month:02}.csv'
        file_path = folder_path + file_name  # create file path
        
        # check if file exists, and read CSV into dataframe if it does
        try:
            df_name = f"df_{year}_{month:02}"
            df = pd.read_csv(file_path)  # read CSV into dataframe
            dfs[df_name] = df  # add dataframe to dictionary with df name as key
            print(f"File {file_name} imported successfully as {df_name}.")
            print(f"Shape: {df.shape}")
        except FileNotFoundError:
            print(f"File {file_name} does not exist. Moving to next month.")

# print the number of dataframes imported
print(f"{len(dfs)} dataframes imported successfully.")


# In[ ]:


# Code Block 2
#     This code block combines dataframes into one and displays column information and shape. 
#     It also converts specific date columns to datetime and year-month-day formats using 
#     Pandas' methods.

# combine all dataframes into one
df_combined = pd.concat(dfs.values(), axis=0)

# view information about columns of df_combined, including min and max of non-object columns
df_combined.info(verbose=True)

# print the shape of the combined dataframe
print(f'Shape of the combined dataframe: {df_combined.shape}')

# convert date columns to datetime format
df_combined['Loan Origination Date'] = pd.to_datetime(df_combined['Loan Origination Date'])
df_combined['Funding Date'] = pd.to_datetime(df_combined['Funding Date'])

# convert date columns to year-month-day format
df_combined['Loan Origination Date'] = df_combined['Loan Origination Date'].dt.strftime('%Y-%m-%d')
df_combined['Funding Date'] = df_combined['Funding Date'].dt.strftime('%Y-%m-%d')


# In[ ]:


# Code Block 3
#     This Python code block prompts the user to choose between generating dataframes 
#     only or exporting them as CSV files. It then creates monthly dataframes and 
#     exports them to a CSV file with a formatted filename if the user chooses to do so.

# Define the output folder for CSV exports
output_folder = "OUTPUT DIRECTORY HERE"

# Prompt the user for an option
print("What would you like to do?")
print("Enter 1 to generate dfs only")
print("Enter 2 to generate dfs and export as CSV")
option = input("> ")

# Define the years and months to loop through
years = [2019, 2020, 2021]
months = range(1, 13)

# Loop through each year and month to create and export monthly DataFrames
for year in years:
    for month in months:
        # Filter the data for the current year and month
        monthly_data = df_combined[(df_combined['Funding Date'].dt.year == year) & (df_combined['Funding Date'].dt.month == month)]
        # Create a new DataFrame with the filtered data
        df_monthly = pd.DataFrame(monthly_data)
        # Add a leading zero to the month value if it is a single digit
        month_str = str(month).zfill(2)
        # Print a message indicating that the DataFrame has been created
        print(f"Created df_monthly_{year}_{month_str}")
        if option == '2':
            # Export the DataFrame to a CSV file with the formatted filename
            filename = f"df_monthly_{year}_{month_str}.csv"
            df_monthly.to_csv(output_folder + filename, index=False)
            # Print a message indicating where the file has been saved
            print(f"Exported df_monthly_{year}_{month_str} to {output_folder}{filename}")
            
# Print a message indicating the program has finished
if option == '1':
    print("Dataframes generated successfully.")
elif option == '2':
    print("Dataframes generated and exported as CSV files successfully.")
else:
    print("Invalid option selected.")


# In[ ]:




