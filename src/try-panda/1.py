import pandas as pd
import json
import argparse
import os

# FILE_PATH = 'FSI-2023-DOWNLOAD.xlsx'
# OUTPUT_FILE = 'data.json'

def excel_to_dict(file_path, sheet_name = 0):
    """read excel file and return a list of dictionaries"""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(df.shape)

    result = df.to_dict(orient='records')
    return result

def write_to_json(data, output_file):
    """write data to json file"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Process an Excel file and output JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file')
    args = parser.parse_args()

    data = excel_to_dict(args.input_file)
    countryData = dict()
    for item in data:
        if 'Country' in item:
            countryData[item['Country']] = item
    
    write_to_json(countryData, args.output_file)

if __name__ == '__main__':
    main()