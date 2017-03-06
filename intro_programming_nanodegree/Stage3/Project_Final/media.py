import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__ (self, movie_title, poster_image, trailer_youtube, movie_director, movie_screenwriters, movie_relase_date):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.screenwriters = movie_screenwriters
        self.relase_date = movie_relase_date
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)