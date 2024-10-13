import pandas as pd
import argparse
import os
import matplotlib.pyplot as plt

BEGAIN_DATE = "2015-01-01"
TARGET_COLUMNS = ['Date', 'Crude Oil petroleum', 'Aluminum', 'Bananas', 'Cocoa beans', 'Rubber']

def read_csv_file(file_path):
    print(">>> basename:", os.path.basename(file_path))
    # df = pd.read_csv(file_path, index_col=0)
    df = pd.read_csv(file_path)
    return df

def print_table_size(df):
    print(f"Table size: {df.shape[0]} rows and {df.shape[1]} columns")

def process_data(df):
    # print(df.columns)
    df_subset = df[df['Date'] >= BEGAIN_DATE]
    # print(df_subset.shape)
    # for col in TARGET_COLUMNS:
    #     print(f"Column: {col}")
    #     print(df_subset[col].describe())
    #     print("*"*50)
    df_subset = df_subset[TARGET_COLUMNS].copy()
    df_subset.index = df_subset['Date']
    print(df_subset.head(5))
    print_table_size(df_subset)
    # df_subset.to_html('output.html', index=False)
    # print(df_subset.iloc[0, 0], df_subset.iloc[0, 1])
    print(df_subset.iloc[:,1], type(df_subset.iloc[:,1]))
    average_price = sum(df_subset.iloc[:,1])/len(df_subset.iloc[:,1])
    print(f"Average Price for Crude Oil is {average_price:.6f}")

    df_subset['Oil Price Diff'] = df_subset['Crude Oil petroleum'].diff()
    cols = df_subset.columns.tolist()
    cols.insert(cols.index('Crude Oil petroleum') + 1, cols.pop(cols.index('Oil Price Diff')))  
    df_subset = df_subset[cols] # reorder columns
    print(df_subset.head(5))
    df_subset['Crude Oil petroleum'].plot()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file and output JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')
    args = parser.parse_args()

    df = read_csv_file(args.input_file)
    print(df.shape)
    process_data(df)

if __name__ == '__main__':
    main()