import sqlite3

def load_data(df, db_path):
    print("📤 Loading data into SQLite database...")

    conn = sqlite3.connect(db_path)
    df.to_sql("employees", conn, if_exists="replace", index=False)

    conn.close()
    print("Data loaded successfully.")
