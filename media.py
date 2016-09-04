class Movie(object):
    """A class representing A movie as an object."""

    def __init__(self, trailer_youtube_url, title, poster_image_url,
                 release_date):
        """The movie object constructor.

        Args:
            trailer_youtube_url (str): movie youtube trailer url
            title (str): title of movie
            poster_image_url (str): movie poster image url
            release_date (str): movie release date
        """
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
        self.release_date = release_date
