import pandas as pd
import os

def explore_data(file_path):
    # Print the CSV
    print("Explorint the CSV file")

    if not os.path.exists(file_path):
        print("ERROR: File not found.")
        return
    
    # Load the dataset
    df = pd.read_csv(file_path, low_memory=False)

    # Print the shape
    print("\nDataFrame shape")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    # Print column names and data types
    print("\n Columns and Data types")
    print(df.dtypes)

    # Print null counts
    print("\nNull counts per column")
    print(df.isnull().sum())

    print("\nSample")
    pd.set_option('display.max_columns', None)
    print(df.head())


if __name__ == "__main__":
    CSV_PATH = r"C:\Users\alber\OneDrive\Escritorio\DATA\Python\goverment-etl\data\raw\contract_awards_in_investment_project_financing.csv"
    explore_data(CSV_PATH)