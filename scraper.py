# =========================================================
# College Ranking Analysis using Scraped Data
# =========================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd

# =========================================================
# WEBSITE URL
# =========================================================

url = "https://www.4icu.org/in/"

# =========================================================
# SEND REQUEST
# =========================================================

headers = {
    "User-Agent":
    "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)

# =========================================================
# PARSE HTML
# =========================================================

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# =========================================================
# FIND TABLE
# =========================================================

table = soup.find("table")

# =========================================================
# FIND ALL ROWS
# =========================================================

rows = table.find_all("tr")

# =========================================================
# STORE DATA
# =========================================================

college_data = []

# =========================================================
# LOOP THROUGH ROWS
# =========================================================

for row in rows[1:]:

    cols = row.find_all("td")

    if len(cols) >= 3:

        rank = cols[0].text.strip()

        college = cols[1].text.strip()

        location = cols[2].text.strip()

        college_data.append([
            rank,
            college,
            location
        ])

# =========================================================
# CREATE DATAFRAME
# =========================================================

df = pd.DataFrame(
    college_data,
    columns=[
        "Rank",
        "College_Name",
        "Location"
    ]
)

# =========================================================
# DISPLAY OUTPUT
# =========================================================

print("\nDataset Loaded Successfully\n")

print(df.head())

# =========================================================
# SAVE CSV
# =========================================================

df.to_csv(
    "college_rankings.csv",
    index=False
)

# =========================================================
# SUCCESS MESSAGE
# =========================================================

print(
    "\n✅ College Ranking Data "
    "Scraped Successfully"
)