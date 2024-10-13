import pandas as pd
import argparse

def read_excel_file(file_path, sheet_name = 0):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file and output JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')
    args = parser.parse_args()

    df = read_excel_file(args.input_file)
    # df.shape returns the number of rows and columns in the dataframe
    # print(df.shape)
    print(df.dtypes) # returns the data types of the columns
    # df.columns returns the column names
    print(f"there are {len(df.columns)} in the dataFrame")
    for colName in df.columns:
        print(colName)

    # print(df['P3: Human Rights'].max())
    print(df.nlargest(10, 'P3: Human Rights'))
    print("*"*50)
    for rowData in df.nlargest(1, 'P3: Human Rights').itertuples():
        for field in rowData._fields:
            print(f"{field}: {getattr(rowData, field)}")
        # print(rowData)
        # print(type(rowData), len(rowData), rowData)

    # df.to_html('output.html')

if __name__ == '__main__':
    main()