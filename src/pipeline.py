from extract import extract_data
from transform import transform_data
from load import load_data
import pandas as pd

FILE_PATH = "../data/input_data.csv"
DB_PATH = "../database/etl_database.db"
OUTPUT_CSV = "../data/cleaned_data.csv"

def run_pipeline():
    print("\n🚀 Starting ETL Pipeline...\n")

    # Extract
    df = extract_data(FILE_PATH)

    # Transform
    df = transform_data(df)

    # Save cleaned CSV
    df.to_csv(OUTPUT_CSV, index=False)

    # Load
    load_data(df, DB_PATH)

    print("\n🎉 ETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()
