"""
TrendPulse - Task 2: Data Processing

Cleans the raw trending data, removes duplicates, handles missing values,
converts data types, and creates useful derived columns.
"""

import pandas as pd


INPUT_FILE = "trends_raw.csv"
OUTPUT_FILE = "trends_clean.csv"


def clean_data(input_file=INPUT_FILE):
    df = pd.read_csv(input_file)

    # Remove exact duplicate records.
    df = df.drop_duplicates(subset="id")

    # Clean text columns.
    df["title"] = df["title"].fillna("Unknown title").astype(str).str.strip()
    df["author"] = df["author"].fillna("Unknown").astype(str).str.strip()
    df["url"] = df["url"].fillna("").astype(str).str.strip()

    # Convert numeric columns safely.
    for column in ["rank", "id", "score", "comments"]:
        df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

    # Convert Unix timestamp to readable UTC datetime.
    df["published_at"] = pd.to_datetime(
        pd.to_numeric(df["time"], errors="coerce"),
        unit="s",
        errors="coerce",
        utc=True
    )

    # Add simple derived metrics.
    df["engagement"] = df["score"] + df["comments"]
    df["title_length"] = df["title"].str.len()

    # Remove rows without a valid title.
    df = df[df["title"].str.len() > 0]

    # Sort by rank and reset the index.
    df = df.sort_values("rank").reset_index(drop=True)

    return df


if __name__ == "__main__":
    cleaned = clean_data()
    cleaned.to_csv(OUTPUT_FILE, index=False)

    print(f"Processed {len(cleaned)} records.")
    print("Saved: trends_clean.csv")
