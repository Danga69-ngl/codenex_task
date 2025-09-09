import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('tmdb_5000_movies.csv')

def parse_json_column(text):
    try:
        items = json.loads(text.replace("'", '"'))
        return [item['name'] for item in items]
    except:
        return []

movies['genres'] = movies['genres'].apply(parse_json_column)
movies['keywords'] = movies['keywords'].apply(parse_json_column)

movies['cast'] = [[] for _ in range(len(movies))]

def combine_features(row):
    return ' '.join(row['genres']) + ' ' + ' '.join(row['keywords']) + ' ' + ' '.join(row['cast']) + ' ' + (row['overview'] if pd.notnull(row['overview']) else '')

movies['combined_features'] = movies.apply(combine_features, axis=1)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

title_to_index = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend_movies(title, cosine_sim=cosine_sim):
    if title not in title_to_index:
        return f"The movie '{title}' was not found in the dataset."
    
    idx = title_to_index[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    recommended_titles = movies['title'].iloc[movie_indices].values
    return recommended_titles

if __name__ == "__main__":
    print("Movie Recommendation System")
    print("=" * 50)
    
    while True:
        movie_name = input("\nEnter a movie title to get recommendations (or type 'quit' to exit): ").strip()
        
        if movie_name.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using the Movie Recommendation System.")
            break
        
        if not movie_name:
            print("No movie title entered. Please try again.")
            continue
        
        print(f"\nSearching for movies similar to '{movie_name}'...")
        recommendations = recommend_movies(movie_name)
        
        if isinstance(recommendations, str):
            print(f"\n{recommendations}")
            print("Please verify the spelling or try a different title.")
        else:
            print(f"\nTop 5 movies similar to '{movie_name}':")
            print("-" * 50)
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
            print("-" * 50)
