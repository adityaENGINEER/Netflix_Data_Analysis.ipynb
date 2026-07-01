# 🎬 Netflix Movie Data Analysis

An exploratory data analysis (EDA) project that cleans, transforms, and visualizes a Netflix movie dataset to uncover trends in genre popularity, ratings, and release years.

## 📋 Overview

This project walks through a full data-cleaning and exploratory analysis pipeline on a movie dataset, answering questions such as:

- What is the most frequent genre of movies released on Netflix?
- Which rating category (popular, average, below average, not popular) has the highest vote count?
- What movie achieved the highest and lowest popularity scores?
- Which year had the most films released?

## 📁 Dataset

The analysis uses `mymoviedb.csv`, which includes the following columns:

| Column | Description |
|---|---|
| `Release_Date` | Original release date of the movie |
| `Title` | Movie title |
| `Overview` | Short synopsis (dropped during cleaning) |
| `Popularity` | Popularity score |
| `Vote_Count` | Number of votes received |
| `Vote_Average` | Average rating |
| `Original_Language` | Original language (dropped during cleaning) |
| `Genre` | One or more genres, comma-separated |
| `Poster_Url` | Poster image URL (dropped during cleaning) |

> **Note:** The CSV file is not included in this repository. Place `mymoviedb.csv` in the project root before running the notebook.

## 🧹 Data Cleaning Steps

1. Checked for missing values and duplicates (dataset was already clean of both).
2. Converted `Release_Date` to datetime and extracted the release **year**.
3. Dropped low-value columns for analysis: `Overview`, `Original_Language`, `Poster_Url`.
4. Binned `Vote_Average` into four categories — `not_popular`, `below_avg`, `average`, `popular` — using quartile-based cutoffs.
5. Split the comma-separated `Genre` column into lists and **exploded** the dataframe so each row represents a single genre per movie.
6. Cast `Genre` to a categorical data type for memory efficiency and analysis.

## 📊 Visualizations

The notebook produces the following plots using `seaborn` and `matplotlib`:

- **Genre distribution** — count plot showing frequency of each genre.
- **Vote average distribution** — count plot across rating categories.
- **Release year distribution** — histogram of movies released per year.

It also identifies the single most and least popular movies in the dataset.

## 🛠️ Technologies Used

- Python 3
- pandas
- numpy
- matplotlib
- seaborn



## 📈 Key Insights

- The dataset originally contains 9,827 rows and 9 columns, with no missing values or duplicates.
- After cleaning, genres were exploded into individual rows, giving a clearer per-genre distribution.
- Vote averages were bucketed into four intuitive categories for easier comparison.
- Visualizations reveal which genres dominate the catalog and which years had peak movie releases.

## 📝 Conclusion

This project cleaned and prepared a raw movie dataset for analysis by removing unnecessary columns, handling data types, and restructuring genre data. Exploratory analysis and visualizations then surfaced insights into movie popularity, ratings, genre distribution, and release trends — providing a foundation for data-driven decision making.


