
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Netflix Business Insights",
    page_icon="🎬",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("/content/netflix_titles_cleaned.csv")

df = load_data()

# Dashboard heading
st.title("🎬 Netflix Business Insights Dashboard")
st.markdown(
    "Explore Netflix content trends, geographic distribution "
    "and business opportunities using data science."
)

st.divider()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

content_type = st.sidebar.multiselect(
    "Content Type",
    options=sorted(df["type"].dropna().unique()),
    default=sorted(df["type"].dropna().unique())
)

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())

year_range = st.sidebar.slider(
    "Release Year",
    min_year,
    max_year,
    (min_year, max_year)
)

filtered_df = df[
    df["type"].isin(content_type) &
    df["release_year"].between(*year_range)
].copy()

# KPI metrics
st.subheader("📊 Catalogue Overview")

total_countries = (
    filtered_df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .nunique()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{len(filtered_df):,}")
col2.metric(
    "Movies",
    f"{(filtered_df['type'] == 'Movie').sum():,}"
)
col3.metric(
    "TV Shows",
    f"{(filtered_df['type'] == 'TV Show').sum():,}"
)
col4.metric("Countries", f"{total_countries:,}")

st.divider()

# Content distribution
st.subheader("📺 Content Distribution")

left, right = st.columns(2)

with left:
    type_counts = filtered_df["type"].value_counts()

    fig = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        hole=0.45,
        title="Movies vs TV Shows"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    yearly = (
        filtered_df.groupby("release_year")
        .size()
        .reset_index(name="titles")
    )

    fig = px.line(
        yearly,
        x="release_year",
        y="titles",
        markers=True,
        title="Titles by Release Year"
    )

    st.plotly_chart(fig, use_container_width=True)

# Genre analysis
st.subheader("🎭 Genre Analysis")

genre_data = filtered_df.assign(
    genre=filtered_df["listed_in"].str.split(", ")
).explode("genre")

genre_counts = (
    genre_data["genre"]
    .dropna()
    .value_counts()
    .head(10)
    .reset_index()
)

genre_counts.columns = ["Genre", "Titles"]

fig = px.bar(
    genre_counts.sort_values("Titles"),
    x="Titles",
    y="Genre",
    orientation="h",
    title="Top 10 Netflix Genres"
)

st.plotly_chart(fig, use_container_width=True)

# Geographic analysis
st.subheader("🌍 Geographic Analysis")

country_data = filtered_df.assign(
    country=filtered_df["country"].str.split(", ")
).explode("country")

country_counts = (
    country_data["country"]
    .dropna()
    .value_counts()
    .head(10)
    .reset_index()
)

country_counts.columns = ["Country", "Titles"]

fig = px.bar(
    country_counts.sort_values("Titles"),
    x="Titles",
    y="Country",
    orientation="h",
    title="Top 10 Content-Producing Countries"
)

st.plotly_chart(fig, use_container_width=True)

# Catalogue explorer
st.subheader("🔎 Explore Netflix Catalogue")

search = st.text_input("Search for a title")

explorer_df = filtered_df.copy()

if search:
    explorer_df = explorer_df[
        explorer_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

display_columns = [
    "title",
    "type",
    "release_year",
    "country",
    "rating",
    "listed_in"
]

st.dataframe(
    explorer_df[display_columns],
    use_container_width=True,
    hide_index=True
)

# Download filtered data
csv = explorer_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered Dataset",
    data=csv,
    file_name="netflix_filtered_data.csv",
    mime="text/csv"
)

st.divider()

st.caption(
    "Netflix Content Analytics | Advanced Data Science Project"
)
