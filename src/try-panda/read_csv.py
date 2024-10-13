import pandas as pd
import argparse
import os

def read_csv_file(file_path):
    print("basename:", os.path.basename(file_path))
    df = pd.read_csv(file_path)
    return df

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file and output JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')
    args = parser.parse_args()

    df = read_csv_file(args.input_file)
    print(df.shape)
    print(df.dtypes)

    print(df.columns)
    df_subset = pd.concat([df.iloc[:, :4], df.iloc[:, -6:-1]], axis=1)
    print(df_subset.head(5))
    df_subset.to_html(f'{os.path.splitext(os.path.basename(args.input_file))[0]}.html')

if __name__ == '__main__':
    main()