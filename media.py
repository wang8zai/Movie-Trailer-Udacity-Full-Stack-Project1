import webbrowser


class Movie():
    """a class specify the movie properites that will show
    on movie trailer website.

    Attributes:
        self.title(str): keep movie title here. Will be
        displayed on website with its poster.
        self.storyline(str): Description of the movie is kept here.
        self.poster_image_url(str): movie poster url is kept here.
        self.trailer_youtube_url(str): trailer url is kept here.
    """
    def __init__(self, movie_title, movie_storyline,
                 movie_poster, movie_trailer):
        """Moive class constructor.

        Arguments:
            self(Movie): the movie instance.
            movie_title(str): keep movie_title int self.title.
            Specify movie title.
            movie_storyline(str): specify movie description in a few lines.
            movie_poster(str): keep a movie poster url in
            self.poster_image_url. Will be shown on website.
            movie_trailer(str): actual tariler video url that will be
            linked to on trailer website.
        No return values.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def showTrailer(self):
        """Will show the trailer website once
        taken a movie instance as argument.
        Arguments:
            self: the movie class instance.
        Return:
            No return.
        """
        webbrowser.open(self.trailer_youtube_url)
        """Will open trailer_youtoube_url string as website.
        And will display that website.
        """
