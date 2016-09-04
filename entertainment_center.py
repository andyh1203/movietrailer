from fresh_tomatoes import open_movies_page
from media import Movie

# Create list of trailer youtube urls
trailer_youtube_urls = [
    'https://www.youtube.com/watch?v=m8e-FF8MsqU',
    'https://www.youtube.com/watch?v=66TuSJo4dZM',
    'https://www.youtube.com/watch?v=JMiFsFQcFLE'
]

# Create list of movie titles
titles = [
    'The Matrix',
    'Inception',
    'Rush Hour'
]

# Create list of poster image urls
poster_image_urls = [
    'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
    'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_(2010)_theat'
    'rical_poster.jpg',
    'http://ia.media-imdb.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcw'
    'NjU3MTc0MQ@@._V1_UY268_CR4,0,182,268_AL_.jpg'
]

# Create list of movie release dates
release_dates = [
    'March 31, 1999',
    'July 13, 2010',
    'September 18, 1998',
]

# Create list of movies objects via list comprehension
movies = [Movie(trailer_youtube_urls[i], titles[i], poster_image_urls[i],
                release_dates[i]) for i in range(3)]

# Function call to generate HTML file and open in browser
open_movies_page(movies)
