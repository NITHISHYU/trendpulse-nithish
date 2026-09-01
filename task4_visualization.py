"""
TrendPulse - Task 4: Visualization

Creates visualisations from the cleaned trending data.
The charts are saved as PNG files.
"""

import pandas as pd
import matplotlib.pyplot as plt


INPUT_FILE = "trends_clean.csv"


def create_visualizations(input_file=INPUT_FILE):
    df = pd.read_csv(input_file)

    # 1. Top stories by score.
    top_score = df.nlargest(10, "score").sort_values("score")

    plt.figure(figsize=(10, 6))
    plt.barh(top_score["title"], top_score["score"])
    plt.xlabel("Score")
    plt.ylabel("Story")
    plt.title("Top 10 Trending Stories by Score")
    plt.tight_layout()
    plt.savefig("top_stories_by_score.png", dpi=150)
    plt.close()

    # 2. Top stories by comments.
    top_comments = df.nlargest(10, "comments").sort_values("comments")

    plt.figure(figsize=(10, 6))
    plt.barh(top_comments["title"], top_comments["comments"])
    plt.xlabel("Comments")
    plt.ylabel("Story")
    plt.title("Top 10 Trending Stories by Comments")
    plt.tight_layout()
    plt.savefig("top_stories_by_comments.png", dpi=150)
    plt.close()

    # 3. Score vs comments relationship.
    plt.figure(figsize=(8, 6))
    plt.scatter(df["score"], df["comments"], alpha=0.7)
    plt.xlabel("Score")
    plt.ylabel("Comments")
    plt.title("Score vs Comments")
    plt.tight_layout()
    plt.savefig("score_vs_comments.png", dpi=150)
    plt.close()

    print("Created:")
    print("- top_stories_by_score.png")
    print("- top_stories_by_comments.png")
    print("- score_vs_comments.png")


if __name__ == "__main__":
    create_visualizations()
