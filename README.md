# Most Popular Baby Names in the USA: 140+ Years of Naming Trends

## Project Overview
This project analyzes historical US baby naming trends from 1881 to 2022 using official Social Security Administration (SSA) data. The analysis explores which names have been most popular, how naming preferences have evolved over time, and identifies significant shifts in cultural and naming patterns across 140+ years. The interactive Tableau dashboard makes these trends accessible to researchers, demographers, and anyone curious about American naming history.

**Dataset Source:** [Social Security Administration - Baby Names Data](https://www.ssa.gov/oact/babynames/limits.html)

**Interactive Dashboard:** [Tableau Public - Most Popular Baby Names 1881-2022](https://public.tableau.com/app/profile/long.phan6932/viz/MostPopularBabyNames1881-2022/GenderRatio)

---

## Project Structure

```
MostPopularBabyNames2024/
├── Baby Names USA/
│   ├── babyNamesSince1881.csv.zip              (Raw SSA data)
│   ├── babyNamesSince1881.hyper                (Tableau-optimized extract: 12.2 MB)
│   ├── Most Popular Baby Names 1881-2022.twbx  (Tableau workbook: 7.6 MB)
│   ├── BabyNamesSince1881.twb                  (Tableau workbook: backup)
│   ├── babyNames.ipynb                         (Python notebook: data processing)
│   └── babyNamesSince1881.py                   (Python script: data pipeline)
```

---

## 1. Data Loading & Exploration

### Objective
Import SSA baby names dataset and understand its structure, scale, and characteristics.

### Process
- Load SSA baby names data (1881–2022, 140+ years)
- Inspect dataset dimensions and columns
- Assess data completeness and quality
- Understand data format (names, gender, year, count)

### Key Findings
- **Total Records**: Millions of baby name records across 140+ years
- **Time Span**: 1881–2022 (continuous annual data)
- **Coverage**: Male and female names across all US states
- **Name Diversity**: Thousands of unique names tracked over time
- **Data Quality**: High-quality official government records with minimal gaps

---

## 2. Data Processing & Aggregation

### Objective
Transform raw SSA data into a format suitable for trend analysis and visualization.

### Process

#### **Step 1: Load and Inspect**
- Read SSA baby names CSV files
- Parse year, name, gender, and count columns
- Handle any formatting inconsistencies

#### **Step 2: Aggregate by Year and Gender**
- Group baby names by year and gender
- Sum counts for the same name across states (if data includes state-level granularity)
- Rank names by popularity within each year and gender

#### **Step 3: Calculate Year-Over-Year Trends**
- Track rank changes for individual names over time
- Identify names entering and leaving top rankings
- Calculate popularity growth/decline rates

#### **Step 4: Create Derived Metrics**
- Gender ratio analysis (which names are gender-neutral, how ratios changed)
- Decade-level aggregations for broader trend analysis
- Top 10, Top 50, Top 100 name rankings by decade

#### **Step 5: Optimize for Tableau**
- Create Hyper extract (12.2 MB) for fast dashboard performance
- Prepare normalized dimension and fact tables
- Ensure data supports all dashboard drill-down paths

### Output
- **Processed Dataset**: Aggregated by name, gender, year with ranking and trend data
- **Hyper Extract**: Tableau-optimized format enabling interactive dashboard performance
- **Data Structure**: Ready for multi-dimensional analysis (name → year → gender → rank)

---

## 3. Exploratory Data Analysis (Python Notebook)

### Objective
Understand naming patterns and trends in the processed dataset.

### Analysis Performed

#### **All-Time Popular Names**
- Identified top 100 most popular names across entire 140-year span
- Separated by gender
- Calculated total baby counts per name

#### **Decade Trends**
- Top names by decade (1880s, 1890s, ... 2020s)
- How rankings have shifted across decades
- Entry/exit of names from top rankings

#### **Name Popularity Trajectories**
- Tracked individual names over entire time period
- Identified rising stars (names gaining popularity over time)
- Identified fading names (names declining in popularity)
- Found peak years for individual names

#### **Gender Patterns**
- Analyzed gender ratio shifts (e.g., names becoming more gender-neutral)
- Identified traditionally gendered names
- Tracked how naming conventions changed by gender

#### **Cultural & Historical Insights**
- Impact of major historical events on naming (wars, economic shifts, cultural movements)
- Immigration and ethnic name patterns
- Modern naming trends (2020s preferences vs. historical norms)

### Techniques Used
- **Pandas**: Data loading, groupby aggregations, ranking, merging
- **Python**: Data transformation, filtering, sorting
- **Statistical Analysis**: Trend identification, year-over-year comparisons

---

## 4. Tableau Dashboard: Interactive Naming Trends Analysis

### Objective
Create an accessible, interactive dashboard enabling exploration of 140+ years of US naming trends.

### Dashboard Structure

**10 Worksheets covering:**
- Top 100 most popular names (all-time)
- Top names by decade
- Name popularity rankings over time (line charts)
- Gender ratio analysis
- Rising and declining names
- Name frequency distributions
- Year-by-year comparisons
- Naming trend trajectories for individual names

**4 Dashboards organized by exploration type:**

1. **Gender Ratio Overview** — Analyzes how gender distribution of names has changed; identifies gender-neutral trends

2. **Popularity Trends** — Track individual name popularity over 140+ years; visualize rank changes and peak years

3. **Decade Comparison** — Compare top names across different time periods; see how preferences evolved

4. **Rising & Falling Names** — Identify names gaining popularity and names declining; understand modern vs. historical naming

### Key Features
- **Interactive Filters** — Filter by year range, name type, gender
- **Drill-Down Capability** — Explore from decade-level down to individual year analysis
- **Trend Lines** — Visualize popularity trajectories for individual names
- **Comparative Views** — Side-by-side comparisons of different time periods
- **Search Functionality** — Find specific names and track their popularity journey

### Use Cases
- **Researchers**: Analyze demographic and cultural trends through naming
- **Demographers**: Understand US population shifts and cultural movements
- **Writers/Creatives**: Research authentic name choices for different time periods
- **Genealogists**: Understand naming conventions in historical research
- **General Users**: Explore personal curiosity about naming trends and history

---

## Technical Skills Demonstrated

### Data Engineering
- Loading and processing large government datasets
- Multi-year data aggregation and time-series preparation
- Creating optimized data extracts for BI tools
- Ranking and trend calculation algorithms
- Data normalization for dimensional analysis

### Data Visualization & BI
- Tableau dashboard design with 140+ year historical data
- Interactive filtering and temporal navigation
- Trend visualization (line charts for popularity trajectories)
- Comparative analysis views (decade-to-decade, gender comparisons)
- Public-facing dashboard design for broad audience

### Data Analysis
- Trend identification and time-series analysis
- Ranking and sorting algorithms
- Gender and demographic pattern analysis
- Historical pattern recognition

---

## Key Insights & Findings

1. **Dramatic Shifts in Popular Names**: Top names from 1880s (Mary, John) are very different from 2020s (Olivia, Liam), reflecting cultural and social changes

2. **Gender Neutralization**: Some names have become increasingly gender-neutral over time (e.g., names becoming unisex where they were once gendered)

3. **Cyclical Trends**: Some names experience cycles of popularity, fading and then re-emerging years later

4. **Immigration Patterns**: Name diversity and ethnic name adoption patterns reflect US immigration waves

5. **Modern Uniqueness**: Recent decades show increasing name diversity—fewer babies share the #1 most popular name compared to historical averages

6. **Decade-Specific Preferences**: Each decade has distinct naming preferences, reflecting contemporary culture, media, and social trends

---

## Files & Deliverables

| File | Size | Purpose |
|------|------|---------|
| `babyNamesSince1881.csv.zip` | Variable | Raw SSA baby names data |
| `babyNamesSince1881.hyper` | 12.2 MB | Tableau-optimized data extract for dashboard performance |
| `Most Popular Baby Names 1881-2022.twbx` | 7.6 MB | Tableau workbook (packaged with data) |
| `BabyNamesSince1881.twb` | Small | Tableau workbook (requires separate data connection) |
| `babyNames.ipynb` | ~12 KB | Python notebook with data processing and analysis code |
| `babyNamesSince1881.py` | ~1 KB | Python script for data pipeline automation |

---

## How to Use This Project

### Explore the Dashboard
1. Visit [Tableau Public Dashboard](https://public.tableau.com/app/profile/long.phan6932/viz/MostPopularBabyNames1881-2022/GenderRatio)
2. Use interactive filters to explore by year range, gender, name type
3. Drill down from decade-level trends to individual year analysis
4. Search for specific names to track their popularity journey
5. Share insights or export views for research/presentations

### Reproduce the Analysis
1. Download SSA baby names data from [SSA website](https://www.ssa.gov/oact/babynames/limits.html)
2. Run `babyNames.ipynb` to reproduce data processing and analysis steps
3. Connect Tableau to processed dataset to rebuild or modify dashboards

### Extend the Project
- Add state-level analysis (which states preferred which names)
- Incorporate census data to correlate naming with demographic shifts
- Build predictive model for future naming trends
- Add regional/ethnic name analysis
- Analyze name longevity and generational patterns

---

## Tools & Technologies Used

- **Data Processing**: Python, Pandas, Jupyter Notebook
- **Data Visualization**: Tableau Public
- **Data Format**: CSV, Hyper (Tableau optimized format)
- **Data Source**: Social Security Administration (official US government records)

---

## Notes

- Data covers 1881–2022 (141 years of continuous records)
- Dashboard is publicly accessible on Tableau Public
- SSA data includes all names given to 5+ babies in a year (privacy protection)
- Analysis captures broader trends; individual names may have incomplete historical coverage for years with very low counts

---

## Contact & Attribution

Project demonstrates data engineering, time-series analysis, and business intelligence visualization skills applied to historical demographic data for public insight and research.

**Repository**: [GitHub - MostPopularBabyNames2024](https://github.com/baolongphan-oss/MostPopularBabyNames2024)

**Published Dashboard**: [Tableau Public - Most Popular Baby Names](https://public.tableau.com/app/profile/long.phan6932/viz/MostPopularBabyNames1881-2022/GenderRatio)
