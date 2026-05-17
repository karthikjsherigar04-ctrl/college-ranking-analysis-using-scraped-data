# College Ranking Analysis using Scraped Data

<p align="center">
  <img src="top10_colleges.png" width="850">
</p>

<p align="center">
  <b>Web Scraping • Data Cleaning • Exploratory Data Analysis • Data Visualization</b>
</p>

---

# Project Overview

This project performs **College Ranking Analysis** using data collected through **Web Scraping** techniques in Python. The project extracts engineering college ranking information, cleans and preprocesses the dataset, and generates insightful visualizations to analyze ranking patterns among top engineering institutions in India.

The workflow demonstrates the practical implementation of:

- Web Scraping
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Python Automation

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Pandas | Data Cleaning & Analysis |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| WordCloud | Text Visualization |
| BeautifulSoup / Selenium | Web Scraping |

---

# Dataset Source

Data collected from engineering college ranking websites and educational sources.

---

# Project Workflow

```text
Web Scraping
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Visualization & Insights
```

---

# Project Structure

```bash
college-ranking-analysis-using-scraped-data/
│
├── scraper.py
├── cleaned_data.py
├── analysis.py
│
├── raw_college_data.csv
├── cleaned_college_data.csv
│
├── top10_colleges.png
├── rank_distribution.png
├── top5_piechart.png
├── iit_vs_nit.png
├── college_types.png
├── wordcloud.png
├── rank_trend.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Features

- Scrapes engineering college ranking data
- Cleans and preprocesses collected data
- Performs ranking analysis
- Generates professional visualizations
- Identifies IIT, NIT, IIIT distributions
- Creates WordCloud analysis for colleges
- Saves charts automatically

---

# Step 1 : Web Scraping

The scraping module extracts:

- College Rank
- College Name
- Institute ID / Location

### Output

```bash
raw_college_data.csv
```

---

# Step 2 : Data Cleaning

The cleaning module performs:

- Duplicate removal
- Missing value handling
- Data type conversion
- Text preprocessing
- Index resetting

### Output

```bash
cleaned_college_data.csv
```

---

# Step 3 : Data Visualization & Analysis

The analysis module generates multiple visual insights.

---

# Visualizations

## 1. Top 10 Engineering Colleges

<p align="center">
  <img src="top10_colleges.png" width="750">
</p>

Displays the top-ranked engineering colleges using a professional gradient bar chart.

---

## 2. Rank Distribution Analysis

<p align="center">
  <img src="rank_distribution.png" width="750">
</p>

Shows the overall distribution of college rankings using histogram and KDE analysis.

---

## 3. Top 5 Colleges Pie Chart

<p align="center">
  <img src="top5_piechart.png" width="650">
</p>

Visual representation of the top 5 engineering colleges.

---

## 4. IIT vs NIT Distribution

<p align="center">
  <img src="iit_vs_nit.png" width="650">
</p>

Compares the number of IITs and NITs in the ranking dataset.

---

## 5. College Type Distribution

<p align="center">
  <img src="college_types.png" width="750">
</p>

Displays the distribution of IIT, NIT, IIIT, and other institutions.

---

## 6. College Name WordCloud

<p align="center">
  <img src="wordcloud.png" width="850">
</p>

WordCloud visualization highlighting frequently appearing college names.

---

## 7. Rank Trend Analysis

<p align="center">
  <img src="rank_trend.png" width="850">
</p>

Line plot showing ranking trends across institutions.

---

# Key Insights

- IITs dominate the top engineering rankings.
- NITs and IIITs contribute significantly to technical education.
- Ranking distribution highlights concentration among premier institutes.
- WordCloud analysis emphasizes frequently appearing institutions.
- Visualization helps identify institutional trends effectively.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/college-ranking-analysis-using-scraped-data.git
```

Navigate into the project directory:

```bash
cd college-ranking-analysis-using-scraped-data
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

```txt
pandas
matplotlib
seaborn
wordcloud
beautifulsoup4
selenium
```

---

# How to Run

## Step 1 : Run Web Scraper

```bash
python scraper.py
```

## Step 2 : Clean Dataset

```bash
python cleaned_data.py
```

## Step 3 : Run Analysis & Visualization

```bash
python analysis.py
```

---

# Future Improvements

- Interactive dashboard using Streamlit
- Real-time ranking updates
- Advanced college comparison analytics
- Geographic visualization using maps
- Machine Learning based ranking prediction

---

# Learning Outcomes

This project helped in gaining practical experience in:

- Web Scraping
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Python Automation
- Data Analytics Workflow

---

# Author

## Karthik J

AIML Student | Python Developer | Data Analytics Enthusiast

---

# License

This project is developed for educational and learning purposes.
