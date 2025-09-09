Movie Recommendation System
This project is a simple movie recommendation system that suggests movies similar to a movie you like. It uses information about each movie—such as genres, keywords, and descriptions—to find other movies with similar content.

How It Works
The program loads a dataset containing details about thousands of movies.
It extracts important features like genres and keywords from the data.
These features are combined with the movie’s description into one text string per movie.
The text is converted into numbers using a method called TF-IDF, which helps identify important words.
The system calculates similarity scores between movies based on these numbers.
When you enter a movie title, it finds and recommends the top 5 movies that are most similar.
How to Use
Run the script.
When prompted, type the name of a movie.
The system will display 5 recommended movies similar to your choice.
To exit, type quit, exit, or q.
Notes
The recommendations are based on movie content, not user ratings or reviews.
Make sure to enter movie titles exactly as they appear in the dataset for best results.
