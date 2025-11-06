import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load dataset
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# ---------------------------
# App Layout
# ---------------------------
st.title("CORD-19 Data Explorer")
st.write("An interactive exploration of COVID-19 research papers using metadata.csv")

# ---------------------------
# Interactive Year Range Filter
# ---------------------------
min_year = int(df["year"].min())
max_year = int(df["year"].max())

year_range = st.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(2020, 2021)
)

df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# ---------------------------
# Visualization 1: Publications by Year
# ---------------------------
st.subheader("Publications by Year (Filtered)")

year_counts = df_filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(year_counts.index, year_counts.values, color="skyblue", edgecolor="black")
ax.set_title("Number of Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# ---------------------------
# Visualization 2: Top Journals
# ---------------------------
st.subheader("Top 10 Journals Publishing COVID-19 Research")

top_journals = df_filtered["journal"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,5))
ax.barh(top_journals.index, top_journals.values, color="orange", edgecolor="black")
ax.set_title("Top 10 Journals")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
ax.invert_yaxis()
st.pyplot(fig)

# ---------------------------
# Visualization 3: Sources
# ---------------------------
st.subheader("Top 10 Sources of Papers")

source_counts = df_filtered["source_x"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,5))
ax.barh(source_counts.index, source_counts.values, color="green", edgecolor="black")
ax.set_title("Distribution of Paper Counts by Source")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
ax.invert_yaxis()
st.pyplot(fig)

# ---------------------------
# Show sample of filtered data
# ---------------------------
if st.checkbox("Show filtered data sample"):
    st.write(df_filtered.head(10))
