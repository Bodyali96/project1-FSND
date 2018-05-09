"""
A module to define and store a movie class with his properties.
Usage : entertainment_center.py
"""


class Movie:
    """
    Creating Movie class with it's properties:
    movie_title, poster_image_url, trailer_youtube_id
    """
    def __init__(self, movie_title, movie_imdb_link, movie_storyline, poster_image_url, trailer_youtube_url):
        """
        initializing Movie attributes.

        Args:
        :param movie_title: the name of the movie.
        :param movie_imdb_link: the url of  the IMDb page of the movie.
        :param movie_storyline: a short description for the movie.
        :param poster_image_url: the url of the movie's poster.
        :param trailer_youtube_url: the url of the movie's youtube trailer.
        """
        self.title = movie_title
        self.imdb_link = movie_imdb_link
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
