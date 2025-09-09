Movie Recommendation System
This project is a content-based movie recommendation system that suggests movies similar to a user-provided title. It uses movie metadata such as genres, keywords, and descriptions to find movies with similar content.

Features
Loads and processes movie data from the TMDB 5000 dataset.
Extracts and combines genres, keywords, and overview text.
Converts text data into numerical features using TF-IDF vectorization.
Computes cosine similarity to identify similar movies.
Provides top 5 movie recommendations based on content similarity.
Interactive command-line interface for user input and recommendations.
Requirements
Python 3.x
pandas
scikit-learn
Install dependencies with:

bash

Run
Copy code
pip install pandas scikit-learn
Usage
Place the tmdb_5000_movies.csv dataset in the project directory.
Run the script:
bash

Run
Copy code
python movie_recommender.py
Enter a movie title when prompted to receive recommendations.
Type quit to exit the program.
Notes
The system relies on movie metadata and does not use user ratings.
Ensure movie titles are entered accurately for best results.
License
This project is open source and available under the MIT License.

