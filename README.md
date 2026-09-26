# 📊 Marketing Data Preprocessing & Analytics

> **A complete data preprocessing pipeline for transforming raw marketing campaign data into a clean, validated, analysis-ready dataset.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Analysis-013243?logo=numpy)
![Excel](https://img.shields.io/badge/Excel-Analytics-217346?logo=microsoftexcel)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🚀 Project Overview

This project focuses on the **data collection, cleaning, preprocessing, transformation, and validation** stage of a marketing analytics workflow.

The project uses a publicly available marketing campaign dataset containing advertising performance information such as impressions, clicks, spending, and conversions.

The objective was to take a raw and imperfect dataset and transform it into a **structured, reliable, and analysis-ready dataset** while documenting every major preprocessing decision.

The complete workflow was implemented using **Python, Pandas, NumPy, and Microsoft Excel**.

---

## 🎯 Objectives

The main objectives of this project were to:

* Collect and inspect publicly available marketing campaign data
* Understand the structure and quality of the raw dataset
* Identify missing values and duplicate records
* Detect inconsistent and invalid observations
* Apply appropriate data-cleaning techniques
* Transform variables into useful analytical formats
* Create marketing performance metrics
* Validate the final dataset
* Document the complete preprocessing workflow
* Produce a reproducible analysis-ready dataset

---

## 📂 Dataset

The dataset contains information about advertising campaigns and their performance.

### Dataset Size

| Stage                 |  Rows | Columns |
| --------------------- | ----: | ------: |
| Raw dataset           | 1,155 |      11 |
| Final cleaned dataset |   916 |      16 |

### Main Attributes

| Attribute             | Description                                     |
| --------------------- | ----------------------------------------------- |
| `ad_id`               | Unique advertisement identifier                 |
| `xyz_campaign_id`     | Campaign identifier                             |
| `fb_campaign_id`      | Facebook campaign identifier                    |
| `age`                 | Target audience age group                       |
| `gender`              | Target audience gender                          |
| `interest`            | Interest category                               |
| `Impressions`         | Number of times the advertisement was displayed |
| `Clicks`              | Number of clicks received                       |
| `Spent`               | Advertising spend                               |
| `Total_Conversion`    | Total number of conversions                     |
| `Approved_Conversion` | Approved conversions                            |

### 🌐 Public Data Source

The dataset was obtained from the public **Nadinozz/Sales_Conversion** repository:

https://github.com/Nadinozz/Sales_Conversion

---

## 🧹 Data Cleaning & Preprocessing

The raw dataset contained several data-quality issues. The following preprocessing workflow was applied.

### 1. Column Standardization

Column names were stripped of unnecessary whitespace and standardized for consistent processing.

### 2. Data Type Conversion

Numeric fields were converted to appropriate numeric data types using Pandas.

### 3. Duplicate Removal

Exact duplicate records were identified and removed.

**Duplicate records identified: 12**

### 4. Missing Demographic Values

Missing values in:

* `age`
* `gender`

were replaced with:

`Unknown`

This avoids unnecessarily removing otherwise useful campaign observations.

### 5. Missing Advertising Spend

Missing `Spent` values were handled using the **campaign-level median**.

If a campaign-level median was unavailable, the overall median was used as a fallback.

### 6. Missing Conversion Outcomes

Records with missing:

* `Total_Conversion`
* `Approved_Conversion`

were removed because these are outcome variables and could not be reliably inferred without introducing potentially misleading values.

### 7. Invalid Impressions

Records containing negative impression values were treated as invalid and removed.

### 8. Extreme Spend Values

Extremely large spend values were identified as data-quality anomalies.

Values above:

**$1,000,000**

were removed from the analytical dataset.

---

## 📈 Feature Engineering

Additional marketing performance metrics were calculated to make the dataset more useful for analysis.

### Click-Through Rate

```text
CTR (%) = (Clicks / Impressions) × 100
```

Measures the percentage of impressions that resulted in clicks.

### Cost Per Click

```text
CPC (USD) = Spent / Clicks
```

Measures the average advertising cost for each click.

### Cost Per Thousand Impressions

```text
CPM (USD) = (Spent / Impressions) × 1,000
```

Measures the advertising cost per 1,000 impressions.

### Conversion Rate

```text
Conversion Rate (%) = (Total Conversion / Clicks) × 100
```

Measures the percentage of clicks that resulted in conversions.

### Cost Per Acquisition

```text
CPA (USD) = Spent / Approved Conversion
```

Measures the average advertising cost associated with an approved conversion.

---

## 🔍 Data Quality Validation

After preprocessing, several validation checks were performed.

| Validation Check                                    | Result |
| --------------------------------------------------- | -----: |
| Duplicate rows remaining                            |      0 |
| Clicks greater than impressions                     |      0 |
| Approved conversions greater than total conversions |      0 |
| Final dataset rows                                  |    916 |
| Final dataset columns                               |     16 |

The validation results confirm that the final dataset satisfies the documented structural and logical checks.

---

## 🐍 Reproducible Python Workflow

The preprocessing workflow is available in:

```text
marketing_data_preprocessing.py
```

The script performs the complete workflow:

```text
Raw CSV
   ↓
Load Dataset
   ↓
Data Type Standardization
   ↓
Duplicate Removal
   ↓
Missing Value Handling
   ↓
Invalid Record Removal
   ↓
Outlier / Anomaly Treatment
   ↓
Feature Engineering
   ↓
Data Validation
   ↓
Cleaned CSV
```

The script can be rerun on the raw dataset to reproduce the cleaning process.

---

## 📁 Repository Structure

```text
marketing-data-preprocessing-project/
│
├── 📄 README.md
│
├── 📊 conversion_data_messy.csv
│   └── Original public-source dataset
│
├── 🐍 marketing_data_preprocessing.py
│   └── Python preprocessing and validation script
│
├── 📊 cleaned_marketing_campaign_data.csv
│   └── Final analysis-ready dataset
│
├── 📗 Week1_Marketing_Data_Preprocessing.xlsx
│   ├── Raw_Data
│   ├── Cleaned_Data
│   ├── Data_Profile
│   ├── Cleaning_Log
│   └── Campaign_Summary
│
└── 📄 Week1_Marketing_Data_Preprocessing_Report.docx
    └── Detailed methodology, screenshots,
        preprocessing decisions, validation,
        limitations and conclusion
```

---

## 🛠️ Technology Stack

### Programming

* 🐍 Python

### Data Processing

* Pandas
* NumPy

### Data Analysis & Presentation

* Microsoft Excel

### Documentation

* Microsoft Word
* GitHub

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/marketing-data-preprocessing-project.git
```

### 2. Navigate to the project

```bash
cd marketing-data-preprocessing-project
```

### 3. Install dependencies

```bash
pip install pandas numpy
```

### 4. Run the preprocessing script

```bash
python marketing_data_preprocessing.py
```

The script reads:

```text
conversion_data_messy.csv
```

and generates:

```text
cleaned_marketing_campaign_data.csv
```

---

## 📊 Project Outcome

The preprocessing pipeline transformed the original **1,155-row raw dataset** into a **916-row, 16-column analysis-ready dataset**.

The final dataset contains both the original campaign attributes and additional performance metrics that can be used for further marketing analysis.

The project also maintains a clear separation between:

**Raw Data → Cleaning → Transformation → Validation → Final Dataset**

This makes the workflow easier to understand, reproduce, audit, and extend.

---

## 🔮 Possible Future Improvements

The cleaned dataset can be used as a foundation for further analysis, including:

* Campaign performance comparison
* Customer/audience segmentation
* Conversion funnel analysis
* Campaign ROI analysis
* Interactive dashboards
* Statistical analysis
* Predictive modeling
* Machine learning for conversion prediction
* Marketing budget optimization

Additional campaign attributes such as placement, device, geography, date/time, creative type, or campaign objective could further improve future analysis if such information is available.

---

## ⚠️ Limitations

This project uses a publicly available dataset and therefore may not represent every type of modern digital advertising campaign.

Some records were removed because their conversion outcomes were missing or because their values were identified as invalid or extreme. Missing spend values were estimated using campaign-level medians.

Therefore, the cleaned dataset should be considered an **analysis-ready version of the selected public dataset**, rather than a complete representation of all possible advertising campaigns.

---

## 👤 Author

**Gunjan**

B.Tech — Computer Science & Engineering

Interested in:

* Data Analytics
* Software Testing
* Automation
* Python
* AI & Data Science

---

## ⭐ Project Highlights

```text
✓ Public marketing campaign dataset
✓ 1,155 raw observations
✓ 916 validated observations
✓ Duplicate detection & removal
✓ Missing-value treatment
✓ Data-quality anomaly detection
✓ Marketing metric calculation
✓ Python preprocessing pipeline
✓ Excel-based data organization
✓ Reproducible workflow
✓ Detailed documentation
```

---

## 📌 Project Status

**Completed — Week 1 Marketing Analytics: Data Collection & Preprocessing**

The dataset is now prepared for the next stages of marketing analytics and exploratory analysis.
