def transform_data(df):
    print("🔄 Transforming data...")

    # Drop rows with missing name or city
    df = df.dropna(subset=["name", "city"])

    # Fill missing ages with average
    df["age"] = df["age"].fillna(df["age"].mean())

    # Convert all city names to uppercase
    df.loc[:, "city"] = df["city"].str.upper()


    print("Data transformation completed.")
    return df
