# 🎬 Netflix Business Insights Dashboard

An interactive data science dashboard built with **Python, Streamlit, Pandas, and Plotly** to explore Netflix's content catalogue, identify content distribution patterns, and generate business insights through data visualization.

## 🌐 Live Dashboard

**Explore the interactive dashboard here:**

[Open Netflix Business Insights Dashboard](https://flaring-jockstrap-paprika.ngrok-free.dev/)

> Note: This is a temporary ngrok link hosted through Google Colab. The dashboard is accessible only while the Colab runtime, Streamlit server, and ngrok tunnel remain active.

---

## 📌 Project Overview

The objective of this project is to analyze Netflix's content catalogue and develop an interactive dashboard that makes it easier to understand content distribution, release-year trends, genre patterns, and geographical representation.

The project applies data science techniques to transform raw catalogue data into meaningful visual insights that can support content strategy and business decision-making.

## 🎯 Project Objectives

- Perform exploratory data analysis (EDA) on the Netflix dataset.
- Examine the distribution of Movies and TV Shows.
- Identify trends in content release years.
- Analyze the most frequently represented genres.
- Explore the geographical distribution of Netflix content.
- Develop interactive visualizations and dashboard filters.
- Generate actionable business recommendations.

## 📊 Dataset Description

The project uses a cleaned Netflix titles dataset containing:

| Dataset Information | Value |
|---|---:|
| Total records | 8,790 |
| Total columns | 15 |
| Movies | 6,126 |
| TV Shows | 2,664 |
| Release years | 1925–2021 |
| Missing values | 0 |
| Duplicate records | 0 |

**Key dataset features include:**
- `show_id`: Unique content identifier.
- `type`: Movie or TV Show.
- `title`: Content title.
- `director`: Director information.
- `cast`: Cast members.
- `country`: Country of production.
- `release_year`: Original release year.
- `rating`: Content classification.
- `duration`: Movie duration or number of seasons.
- `listed_in`: Content genres.
- `description`: Content description.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Plotly | Interactive data visualizations |
| Streamlit | Interactive dashboard development |
| Google Colab | Development environment |
| ngrok | Public dashboard access |

## 📈 Dashboard Features

### 1. Catalogue Overview
Displays key performance indicators:
- Total Netflix titles.
- Number of Movies.
- Number of TV Shows.
- Number of countries represented.

### 2. Content Distribution
- Interactive pie chart comparing Movies and TV Shows.
- Line chart showing the distribution of titles by release year.

### 3. Genre Analysis
- Identifies the top 10 genres.
- Visualizes genre representation using horizontal bar charts.

### 4. Geographic Analysis
- Identifies the top 10 content-producing countries.
- Visualizes geographical content distribution.

### 5. Interactive Catalogue Explorer
- Search for Netflix titles.
- Filter content by type and release year.
- Explore catalogue information.
- Download filtered records as a CSV file.

## 💡 Key Business Insights

The exploratory analysis identified several patterns:

1. **Movie representation:** Movies account for approximately 69.69% of the dataset, while TV Shows represent 30.31%.
2. **Geographical representation:** The United States has the largest number of titles in the dataset, followed by India and the United Kingdom.
3. **Genre distribution:** International Movies, Dramas, and Comedies are among the most represented genres.
4. **Release-year trends:** The median release year is 2017, indicating that much of the catalogue consists of relatively recent productions.

These findings describe catalogue representation rather than actual audience preferences or viewing behaviour.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jostina
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy plotly
```

### 3. Add the dataset

Place `netflix_titles_cleaned.csv` in the project directory.

Update the dataset path in `app.py` if necessary:

```python
data = pd.read_csv("/content/netflix_titles_cleaned.csv")
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

## ⚠️ Limitations

- The dataset contains catalogue metadata rather than actual Netflix viewing records.
- The analysis does not measure customer engagement, subscriptions, revenue, or profitability.
- Historical release-year information ends in 2021.
- Multiple countries and genres can be associated with a single title,so category counts may overlap.

## 🔮 Future Improvements

- Integrate machine learning classification models.
- Add model evaluation metrics and confusion matrices.
- Implement K-Means clustering for content segmentation.
- Develop predictive analytics for catalogue trends.
- Expand the dashboard with additional interactive filters.
- Deploy the application permanently using Streamlit Community Cloud.

## 👩‍💻 Author

**Jostina Ndavi**

Data Science | Data Analytics | Machine Learning

GitHub: https://github.com/jostina

Portfolio: https://jostina.github.io/

---

*This project demonstrates an end-to-end data analytics workflow, from data exploration and visualization to interactive dashboard development and business insight generation.*
