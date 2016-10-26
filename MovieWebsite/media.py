import webbrowser

class Movie():
    def __init__(self, title, art, poster_url, youtube_url):
        self.title = title
        self.art = art
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url