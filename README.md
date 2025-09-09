# 🎬 Movie Recommendation System

An intelligent movie recommendation system that uses machine learning to suggest similar movies based on content analysis. Built with Python, pandas, and scikit-learn.

## ✨ Features

- **Interactive Interface**: Enter any movie title to get personalized recommendations
- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity
- **Comprehensive Analysis**: Considers genres, keywords, and movie overviews
- **User-Friendly**: Clean command-line interface with helpful error messages
- **Continuous Usage**: Get recommendations for multiple movies in one session

## 🚀 How It Works

1. **Data Processing**: Loads and processes the TMDB 5000 movies dataset
2. **Feature Extraction**: Combines movie genres, keywords, and overviews into a single feature vector
3. **Vectorization**: Uses TF-IDF to convert text features into numerical vectors
4. **Similarity Calculation**: Computes cosine similarity between all movie pairs
5. **Recommendation**: Finds the 5 most similar movies to your input

## 📋 Prerequisites

- Python 3.7 or higher
- Required Python packages (see requirements.txt)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**:
   - Download `tmdb_5000_movies.csv` from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Place it in the project directory

## 🎯 Usage

Run the recommendation system:

```bash
python project.py
```

**Example interaction**:
```
Movie Recommendation System
==================================================

Enter a movie title to get recommendations (or type 'quit' to exit): Inception

Searching for movies similar to 'Inception'...

Top 5 movies similar to 'Inception':
--------------------------------------------------
1. The Matrix
2. Interstellar
3. Shutter Island
4. Source Code
5. The Prestige
--------------------------------------------------
```

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** which includes:
- Movie titles and overviews
- Genres and keywords
- Release dates and ratings
- Budget and revenue information

## 🔧 Technical Details

- **Algorithm**: Content-based filtering using TF-IDF and cosine similarity
- **Libraries**: pandas, scikit-learn, numpy
- **Data Processing**: JSON parsing for nested movie metadata
- **Similarity Metric**: Cosine similarity for text-based recommendations

## 📁 Project Structure

```
movie-recommendation-system/
├── project.py              # Main recommendation system
├── tmdb_5000_movies.csv    # Movie dataset (download separately)
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for the movie dataset
- [Kaggle](https://www.kaggle.com/) for hosting the dataset
- The scikit-learn community for the machine learning tools

## 📞 Contact

If you have any questions or suggestions, feel free to open an issue or contact me!

---

**Happy Movie Watching! 🍿**
