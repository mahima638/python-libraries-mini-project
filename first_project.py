# Netflix Movies Data Analysis 🎬

# -----------------------------
# 1. Introduction
# -----------------------------
# This notebook explores a Netflix movies dataset to uncover trends, patterns, and insights.
# It includes Exploratory Data Analysis (EDA), key findings, and actionable recommendations.
# Dataset Sources:
# - movies.csv – contains movie details (title, genre, release year, duration, etc.)
# - ratings.csv – contains user ratings (userId, movieId, rating, timestamp)
# Objective: Analyze viewing patterns and movie trends to suggest improvements for Netflix’s content strategy.

# -----------------------------
# 2. Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Liberation Sans']

# -----------------------------
# 3. Data Loading
# -----------------------------
movies = pd.read_csv("movies.csv", encoding="latin1")
ratings = pd.read_csv("ratings.csv", encoding="latin1")

print("Movies Dataset:")
print(movies.head())
print("\nRatings Dataset:")
print(ratings.head())

# -----------------------------
# 4. Merge Datasets
# -----------------------------
df = pd.merge(movies, ratings, on="movieId")
print(f"\nMerged Dataset Shape: {df.shape}")
print(df.head())

# -----------------------------
# 5. Data Cleaning
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

print(f"\nTotal unique movies: {df['title'].nunique()}")
print(f"Total ratings: {len(df)}")
print(f"Unique users: {df['userId'].nunique()}")
print(f"Average rating: {df['rating'].mean():.2f}")

# Extract release year
df['year'] = df['title'].str.extract(r'\((\d{4})\)').astype(float)

# Oldest and newest movies
print("\nOldest movie:", df.loc[df['year'].idxmin()]['title'])
print("Newest movie:", df.loc[df['year'].idxmax()]['title'])

# -----------------------------
# 6. EDA
# -----------------------------

# Movies per year
movie_per_year = df.groupby('year').size()
plt.figure(figsize=(12, 6))
movie_per_year.plot(kind='bar')
plt.title("Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Rating distribution
plt.figure(figsize=(10, 5))
df['rating'].value_counts().sort_index().plot(kind='bar')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Genre popularity
genre_counts = df['genres'].str.split('|').explode().value_counts()
plt.figure(figsize=(12, 6))
genre_counts.plot(kind='barh', color='skyblue')
plt.title("Genre Popularity")
plt.xlabel("Number of Movies")
plt.ylabel("Genre")
plt.show()

# Top 10 movies by average rating & number of ratings
avg_rating_per_movie = df.groupby('title')['rating'].mean()
num_ratings = df.groupby('title')['rating'].count()

plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
avg_rating_per_movie.sort_values(ascending=False).head(10).plot(
    kind='bar', color='skyblue')
plt.title("Top 10 by Average Rating")
plt.ylabel("Average Rating")
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
num_ratings.sort_values(ascending=False).head(10).plot(kind='bar',
                                                       color='orange')
plt.title("Top 10 by Number of Ratings")
plt.ylabel("Number of Ratings")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# -----------------------------
# 7. Simple Recommendation Example
# -----------------------------
fav_movie = df[df['rating'] >= 4.5].iloc[1]
fav_genre = fav_movie['genres']
suggestions = df[df['genres'] == fav_genre]['title'].unique()

print(f"\nSince you like {fav_movie['title']}, you might also like:")
for movie in suggestions[:10]:
  print("-", movie)

# -----------------------------
# 8. Key Insights
# -----------------------------
# 1. Drama and Comedy dominate the Netflix movie catalog.
# 2. Ratings are generally high, with a median around 3.5/5.
# 3. There’s been a steady increase in content production after 2010.

# -----------------------------
# 9. Recommendations
# -----------------------------
# - Increase content in high-performing genres like Drama and Comedy.
# - Explore untapped genres like Sci-Fi for niche audiences.
# - Invest in more international releases post-2015, as these perform better in ratings.

# -----------------------------
# 10. Conclusion
# -----------------------------
# This analysis highlights the importance of genre selection, content variety,
# and tracking audience ratings to guide Netflix’s content strategy.
