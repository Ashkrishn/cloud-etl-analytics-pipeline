import pandas as pd

# -----------------------
# EXTRACT
# -----------------------
input_path = "../data/raw/online_retail_raw.csv"
df = pd.read_csv(input_path)

print(df.columns)
print("Raw data loaded:", df.shape)

# -----------------------
# TRANSFORM
# -----------------------
df = df.dropna(subset=["Customer ID"])
df = df[df["Quantity"] > 0]

df["Revenue"] = df["Quantity"] * df["Price"]
df["OrderDate"] = pd.to_datetime(df["InvoiceDate"])

# -----------------------
# LOAD
# -----------------------
output_path = "../data/processed/online_retail_processed.csv"
df.to_csv(output_path, index=False)

print("Processed data saved:", df.shape)
