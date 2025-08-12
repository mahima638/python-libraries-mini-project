🎬 Movies Data Analysis
📌 Overview
This project analyzes  movies using Python, focusing on uncovering trends, patterns, and insights from movie and ratings datasets.
The goal is to explore viewing patterns, genre popularity, and rating distributions to help improve  content strategy.

📂 Dataset
movies.csv – Contains movie details:

movieId, title, genres

ratings.csv – Contains user ratings:

userId, movieId, rating, timestamp

Data was merged on movieId to create a single analysis-ready dataset.

🛠️ Technologies Used
Python – Data processing & analysis

Pandas – Data cleaning, transformation, grouping

Matplotlib – Data visualization

Jupyter Notebook – Interactive development environment

📊 Key Analysis Steps
Data Cleaning

Removed null values

Extracted release year from movie titles

Counted unique movies, ratings, and users

Exploratory Data Analysis (EDA)

Movies released per year

Rating distribution

Genre popularity ranking

Top movies by average rating & number of ratings

Recommendation Example

Suggested movies based on high-rated genre similarity

📈 Visualizations
Bar Chart – Movies released per year

Bar Chart – Rating distribution

Horizontal Bar Chart – Genre popularity

Side-by-side Bar Charts – Top movies by average rating and ratings count

💡 Key Insights
Drama and Comedy dominate the catalog.

Ratings tend to be above average, median around 3.5/5.

Content production increased significantly after 2010.

📌 Recommendations
Focus more on high-performing genres (Drama, Comedy)

Invest in Sci-Fi & niche genres for untapped audiences

Increase international releases post-2015

🚀 How to Run
bash
Copy
Edit
# Clone the repository
git clone https://github.com/mahima638/python-libraries-mini-project.git

# Navigate to project folder
cd python-libraries-mini-project

# Install dependencies
pip install pandas matplotlib

# Run the notebook
jupyter notebook