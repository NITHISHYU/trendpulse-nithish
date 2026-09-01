"""
TrendPulse - Task 3: Analysis

Analyses the cleaned trending data and produces summary statistics
and rankings for the most engaging stories.
"""

import pandas as pd


INPUT_FILE = "trends_clean.csv"
OUTPUT_FILE = "analysis_summary.csv"


def analyse_data(input_file=INPUT_FILE):
    df = pd.read_csv(input_file)

    total_stories = len(df)
    total_score = int(df["score"].sum())
    total_comments = int(df["comments"].sum())
    average_score = round(df["score"].mean(), 2) if total_stories else 0
    average_comments = round(df["comments"].mean(), 2) if total_stories else 0

    top_score = df.loc[df["score"].idxmax()] if total_stories else None
    top_engagement = (
        df.loc[df["engagement"].idxmax()] if total_stories else None
    )

    summary = pd.DataFrame([
        ["Total stories", total_stories],
        ["Total score", total_score],
        ["Total comments", total_comments],
        ["Average score", average_score],
        ["Average comments", average_comments],
        [
            "Top story by score",
            top_score["title"] if top_score is not None else "N/A"
        ],
        [
            "Top story by engagement",
            top_engagement["title"] if top_engagement is not None else "N/A"
        ],
    ], columns=["metric", "value"])

    return df, summary


if __name__ == "__main__":
    df, summary = analyse_data()

    summary.to_csv(OUTPUT_FILE, index=False)

    print("\nTRENDPULSE ANALYSIS")
    print("===================")
    print(summary.to_string(index=False))

    print("\nTop 10 stories by engagement:")
    print(
        df.nlargest(10, "engagement")[["rank", "title", "score", "comments", "engagement"]]
        .to_string(index=False)
    )

    print(f"\nSaved: {OUTPUT_FILE}")
