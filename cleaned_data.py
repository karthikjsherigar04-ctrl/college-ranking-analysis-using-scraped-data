# =========================================================
# STEP 2 : DATA CLEANING
# =========================================================

import pandas as pd

# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

df = pd.read_csv(
    "college_rankings.csv"
)

# ---------------------------------------------------------
# DISPLAY RAW DATA
# ---------------------------------------------------------

print("\nRAW DATASET\n")

print(df.head())

print("\nDataset Shape:", df.shape)

# ---------------------------------------------------------
# CHECK MISSING VALUES
# ---------------------------------------------------------

print("\nMISSING VALUES\n")

print(df.isnull().sum())

# ---------------------------------------------------------
# REMOVE DUPLICATES
# ---------------------------------------------------------

df.drop_duplicates(inplace=True)

# ---------------------------------------------------------
# REMOVE NULL VALUES
# ---------------------------------------------------------

df.dropna(inplace=True)

# ---------------------------------------------------------
# CLEAN TEXT COLUMNS
# ---------------------------------------------------------

df["College_Name"] = (
    df["College_Name"]
    .astype(str)
    .str.strip()
)

df["Location"] = (
    df["Location"]
    .astype(str)
    .str.strip()
)

# ---------------------------------------------------------
# CONVERT RANK COLUMN
# ---------------------------------------------------------

df["Rank"] = pd.to_numeric(
    df["Rank"],
    errors="coerce"
)

# ---------------------------------------------------------
# REMOVE INVALID RANKS
# ---------------------------------------------------------

df.dropna(subset=["Rank"], inplace=True)

# Convert rank into integer
df["Rank"] = df["Rank"].astype(int)

# ---------------------------------------------------------
# SORT DATA BY RANK
# ---------------------------------------------------------

df.sort_values(
    by="Rank",
    inplace=True
)

# ---------------------------------------------------------
# RESET INDEX
# ---------------------------------------------------------

df.reset_index(
    drop=True,
    inplace=True
)

# ---------------------------------------------------------
# SAVE CLEANED DATASET
# ---------------------------------------------------------

df.to_csv(
    "cleaned_college_data.csv",
    index=False
)

# ---------------------------------------------------------
# DISPLAY CLEANED DATA
# ---------------------------------------------------------

print("\nCLEANED DATASET\n")

print(df.head())

print("\nFinal Dataset Shape:", df.shape)

# ---------------------------------------------------------
# SUCCESS MESSAGE
# ---------------------------------------------------------

print(
    "\n✅ Data Cleaning Completed Successfully"
)