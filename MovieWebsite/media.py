import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, art, trailer, director, actors, release, criterion, criterion_icon):
        self.title = title
        self.poster_image_url = art
        self.trailer_youtube_url = trailer
        self.director = director
        self.actors = actors
        self.release_date = release
        self.criterion = criterion
        self.criterion_icon = criterion_icon