#Part 1 Data Loading and Inspection
import pandas as pd

#Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\user\Desktop\PLP\Framework_assignment\metadata.csv")

# Display the shape and first few rows of the DataFrame
print("first few rows and data structure:")
print(df.head())

# Data Exploration
print("Data Exploration:")
print(df.shape)

# Identify data types of each column
print("\nColumn data types:")
print(df.dtypes)

#Check for missing values in important columns
important_cols = ["title", "abstract", "publish_time", "authors", "journal"]
print("\nMissing values in important columns:")
print(df[important_cols].isnull().sum())

# Generate basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

#Part 2 Data Cleaning and Preparation
# -----------------------------------------------------------
# 1. Identify columns with many missing values
# -----------------------------------------------------------
missing_counts = df.isnull().sum().sort_values(ascending=False)
print("\nMissing values per column:")
print(missing_counts.head(15))   # show top 15 columns with most missing values

# -----------------------------------------------------------
# 2. Handle missing data
# -----------------------------------------------------------
# Drop rows where critical information is missing
df = df.dropna(subset=['title', 'publish_time'])

# Fill missing abstracts with an empty string
df['abstract'] = df['abstract'].fillna("")

# Fill missing journals with "Unknown"
df['journal'] = df['journal'].fillna("Unknown")

# Optional: If authors missing, mark as "Anonymous"
df['authors'] = df['authors'].fillna("Anonymous")

# -----------------------------------------------------------
# 3. Prepare data for analysis
# -----------------------------------------------------------
# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Remove rows where publish_time could not be parsed
df = df.dropna(subset=['publish_time'])

# Extract year for time-based analysis
df['year'] = df['publish_time'].dt.year

# Create new feature: abstract word count
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

# -----------------------------------------------------------
# 4. Save cleaned dataset
# -----------------------------------------------------------
df.to_csv(r"C:\Users\user\Desktop\PLP\Framework_assignment\metadata_cleaned.csv", index=False)

# -----------------------------------------------------------
# 5. Quick checks after cleaning
# -----------------------------------------------------------
print("\n✅ Cleaning complete!")
print("New dataset shape:", df.shape)
print("\nPreview of cleaned data:")
print(df.head())
print("\nRemaining missing values in important columns:")
print(df[['title','abstract','publish_time','authors','journal']].isnull().sum())


#Part 3 Data Analysis and Visualization
import re
from collections import Counter
# Load cleaned dataset
df = pd.read_csv(r"C:\Users\user\Desktop\PLP\Framework_assignment\metadata_cleaned.csv")

# -----------------------------------------------------------
# 1. Count papers by publication year
# -----------------------------------------------------------
papers_by_year = df['year'].value_counts().sort_index()
print("\n📅 Papers per year:")
print(papers_by_year)

# -----------------------------------------------------------
# 2. Identify top journals
# -----------------------------------------------------------
top_journals = df['journal'].value_counts().head(10)
print("\n🏆 Top journals:")
print(top_journals)

# -----------------------------------------------------------
# 3. Most frequent words in titles
# -----------------------------------------------------------
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)  # keep only letters
    return text

all_titles = " ".join(df['title'].dropna().apply(preprocess_text))
word_counts = Counter(all_titles.split())

# Remove common stopwords
stopwords = set([
    "the", "and", "of", "to", "in", "for", "a", "on", "with", 
    "by", "an", "at", "from", "as", "using", "is", "are", "based"
])
filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stopwords}

top_words = Counter(filtered_word_counts).most_common(15)
print("\n🔑 Top words in titles:")
print(top_words)

# -----------------------------------------------------------
# Data Visualization 
import matplotlib.pyplot as plt

# Count publications by year
year_counts = df['year'].value_counts().sort_index()
print("\nYearly publication counts:")
print(year_counts)

# Bar chart of publications by year
plt.figure(figsize=(10,6))
plt.bar(year_counts.index, year_counts.values, color="skyblue", edgecolor="black")
plt.title("Number of Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45)
plt.show()

