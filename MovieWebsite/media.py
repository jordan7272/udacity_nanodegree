import webbrowser

class Movie():
    """Class defintion of Movie object"""
    def __init__(self, title, art, poster_url, youtube_url):
        """Constructor method to create a Movie instance"""
        self.title = title
        self.art = art
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
