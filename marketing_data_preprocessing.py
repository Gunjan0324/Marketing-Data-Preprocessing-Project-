"""
Week 1 - Marketing Data Collection and Preprocessing
----------------------------------------------------
Source dataset:
https://github.com/Nadinozz/Sales_Conversion

Expected input:
    conversion_data_messy.csv

This script reproduces the cleaning and preprocessing workflow documented
in the Week 1 Marketing Analytics report.

Output:
    cleaned_marketing_campaign_data.csv
"""

import pandas as pd
import numpy as np


INPUT_FILE = "conversion_data_messy.csv"
OUTPUT_FILE = "cleaned_marketing_campaign_data.csv"


def load_data(file_path):
    """Load the raw CSV dataset."""
    df = pd.read_csv(file_path)
    return df


def clean_and_preprocess(df):
    """Apply the documented cleaning and transformation steps."""

    # ------------------------------------------------------------
    # 1. Standardize column names
    # ------------------------------------------------------------
    df.columns = df.columns.str.strip()

    # ------------------------------------------------------------
    # 2. Convert numeric columns to numeric data types
    # ------------------------------------------------------------
    numeric_columns = [
        "ad_id",
        "xyz_campaign_id",
        "fb_campaign_id",
        "interest",
        "Impressions",
        "Clicks",
        "Spent",
        "Total_Conversion",
        "Approved_Conversion",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # ------------------------------------------------------------
    # 3. Remove exact duplicate records
    # ------------------------------------------------------------
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    # ------------------------------------------------------------
    # 4. Handle missing demographic values
    # ------------------------------------------------------------
    df["age"] = df["age"].fillna("Unknown")
    df["gender"] = df["gender"].fillna("Unknown")

    # ------------------------------------------------------------
    # 5. Handle missing Spent values
    #    Use campaign-level median first, then global median
    #    as a fallback.
    # ------------------------------------------------------------
    campaign_medians = df.groupby("xyz_campaign_id")["Spent"].transform("median")

    df["Spent"] = df["Spent"].fillna(campaign_medians)
    df["Spent"] = df["Spent"].fillna(df["Spent"].median())

    # ------------------------------------------------------------
    # 6. Remove rows with missing conversion outcomes
    #    These are outcome variables, so they are not imputed.
    # ------------------------------------------------------------
    df = df.dropna(
        subset=["Total_Conversion", "Approved_Conversion"]
    )

    # ------------------------------------------------------------
    # 7. Remove invalid negative impressions
    # ------------------------------------------------------------
    df = df[df["Impressions"] >= 0]

    # ------------------------------------------------------------
    # 8. Remove extreme spend anomalies
    #    Values above $1,000,000 were treated as data-quality
    #    anomalies in this dataset.
    # ------------------------------------------------------------
    df = df[df["Spent"] <= 1_000_000].copy()

    # ------------------------------------------------------------
    # 9. Create marketing performance metrics
    # ------------------------------------------------------------

    # CTR = Clicks / Impressions
    df["CTR (%)"] = np.where(
        df["Impressions"] > 0,
        (df["Clicks"] / df["Impressions"]) * 100,
        np.nan,
    )

    # CPC = Spend / Clicks
    df["CPC (USD)"] = np.where(
        df["Clicks"] > 0,
        df["Spent"] / df["Clicks"],
        np.nan,
    )

    # CPM = Spend / Impressions * 1000
    df["CPM (USD)"] = np.where(
        df["Impressions"] > 0,
        (df["Spent"] / df["Impressions"]) * 1000,
        np.nan,
    )

    # Conversion Rate = Total Conversion / Clicks
    df["Conversion Rate (%)"] = np.where(
        df["Clicks"] > 0,
        (df["Total_Conversion"] / df["Clicks"]) * 100,
        np.nan,
    )

    # CPA = Spend / Approved Conversion
    df["CPA (USD)"] = np.where(
        df["Approved_Conversion"] > 0,
        df["Spent"] / df["Approved_Conversion"],
        np.nan,
    )

    return df, duplicates_removed


def validate_data(df):
    """Run final data-quality checks."""

    duplicate_rows = df.duplicated().sum()
    invalid_clicks = (df["Clicks"] > df["Impressions"]).sum()
    invalid_approved_conversions = (
        df["Approved_Conversion"] > df["Total_Conversion"]
    ).sum()

    print("\nFINAL VALIDATION")
    print("-" * 40)
    print(f"Duplicate rows remaining: {duplicate_rows}")
    print(f"Clicks > Impressions: {invalid_clicks}")
    print(
        "Approved Conversion > Total Conversion: "
        f"{invalid_approved_conversions}"
    )
    print(f"Final rows: {len(df)}")
    print(f"Final columns: {len(df.columns)}")

    return (
        duplicate_rows == 0
        and invalid_clicks == 0
        and invalid_approved_conversions == 0
    )


def main():
    print("Loading raw marketing campaign dataset...")
    raw_df = load_data(INPUT_FILE)

    print(f"Raw rows: {len(raw_df)}")
    print(f"Raw columns: {len(raw_df.columns)}")

    cleaned_df, duplicates_removed = clean_and_preprocess(raw_df)

    print(f"Exact duplicate rows removed: {duplicates_removed}")
    print(f"Cleaned rows: {len(cleaned_df)}")
    print(f"Cleaned columns: {len(cleaned_df.columns)}")

    # Validate final dataset
    is_valid = validate_data(cleaned_df)

    if not is_valid:
        raise ValueError(
            "Validation failed. Review the preprocessing rules "
            "before using the cleaned dataset."
        )

    # Save final cleaned dataset
    cleaned_df.to_csv(OUTPUT_FILE, index=False)

    print("\nPreprocessing completed successfully.")
    print(f"Cleaned dataset saved as: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
