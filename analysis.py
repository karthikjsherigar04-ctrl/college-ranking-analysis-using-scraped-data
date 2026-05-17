# =====================================================
# COLLEGE RANKING ANALYSIS - DATA VISUALIZATION
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("cleaned_college_data.csv")

# =====================================================
# CREATE CHARTS FOLDER
# =====================================================

os.makedirs("charts", exist_ok=True)

# =====================================================
# STYLE SETTINGS
# =====================================================

sns.set_style("whitegrid")

plt.rcParams["figure.figsize"] = (10, 5)

# =====================================================
# 1. TOP 10 COLLEGES BAR CHART
# =====================================================

top10 = df.head(10)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x="Rank",
    y="College_Name",
    data=top10,
    palette="viridis"
)

plt.title(
    "Top 10 Engineering Colleges in India",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Rank", fontsize=12)
plt.ylabel("College", fontsize=12)

plt.tight_layout()

plt.savefig(
    "charts/top10_colleges.png",
    dpi=300
)

plt.show()

# =====================================================
# 2. RANK DISTRIBUTION HISTOGRAM
# =====================================================

plt.figure(figsize=(10, 5))

sns.histplot(
    df["Rank"],
    bins=20,
    kde=True,
    color="skyblue"
)

plt.title(
    "Rank Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Rank", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.tight_layout()

plt.savefig(
    "charts/rank_distribution.png",
    dpi=300
)

plt.show()

# =====================================================
# 3. TOP 5 COLLEGES PIE CHART
# =====================================================

top5 = df.head(5)

colors = sns.color_palette("pastel")

plt.figure(figsize=(8, 8))

plt.pie(
    [1, 1, 1, 1, 1],
    labels=top5["College_Name"],
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
    shadow=True
)

plt.title(
    "Top 5 Engineering Colleges",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "charts/top5_piechart.png",
    dpi=300
)

plt.show()

# =====================================================
# 4. IIT vs NIT ANALYSIS
# =====================================================

iit_count = df["College_Name"].str.contains(
    "Indian Institute of Technology",
    case=False
).sum()

nit_count = df["College_Name"].str.contains(
    "National Institute of Technology",
    case=False
).sum()

print("IIT Count:", iit_count)
print("NIT Count:", nit_count)

labels = ["IIT", "NIT"]
values = [iit_count, nit_count]

plt.figure(figsize=(7, 7))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    colors=["#4facfe", "#ff9a9e"],
    shadow=True,
    startangle=90
)

plt.title(
    "IIT vs NIT Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "charts/iit_vs_nit.png",
    dpi=300
)

plt.show()

# =====================================================
# 5. COLLEGE TYPE DISTRIBUTION
# =====================================================

types = []

for college in df["College_Name"]:

    if "Indian Institute of Technology" in college:
        types.append("IIT")

    elif "National Institute of Technology" in college:
        types.append("NIT")

    elif "IIIT" in college:
        types.append("IIIT")

    else:
        types.append("Other")

df["Type"] = types

plt.figure(figsize=(8, 5))

ax = sns.countplot(
    x="Type",
    data=df,
    palette="Set2"
)

plt.title(
    "College Types Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("College Type", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.tight_layout()

plt.savefig(
    "charts/college_types.png",
    dpi=300
)

plt.show()

# =====================================================
# 6. WORDCLOUD ANALYSIS
# =====================================================

text = " ".join(df["College_Name"])

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    colormap="viridis"
).generate(text)

plt.figure(figsize=(15, 7))

plt.imshow(wordcloud)

plt.axis("off")

plt.title(
    "College Names WordCloud",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "charts/wordcloud.png",
    dpi=300
)

plt.show()

# =====================================================
# 7. RANK TREND LINE PLOT
# =====================================================

plt.figure(figsize=(12, 5))

plt.plot(
    df["Rank"],
    marker="o",
    linewidth=2,
    color="purple"
)

plt.fill_between(
    range(len(df["Rank"])),
    df["Rank"],
    color="violet",
    alpha=0.3
)

plt.title(
    "College Rank Trend",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Index", fontsize=12)
plt.ylabel("Rank", fontsize=12)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "charts/rank_trend.png",
    dpi=300
)

plt.show()

# =====================================================
# FINAL MESSAGE
# =====================================================

print("\n✅ College Ranking Analysis Completed Successfully")
print("✅ All charts saved inside 'charts' folder")