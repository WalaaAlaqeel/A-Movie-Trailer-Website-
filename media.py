# webbrowser: provides interface to allow displaying Web-based documents to users
import webbrowser

# class Movie(): This class provides a way to store more related information
class Movie():
# __init__ (): this function creates space for that instance.
# The instance will have the format:( movie_title, poster_image, trailer_link)
    def __init__(self, movie_title, poster_image, trailer_link):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link

# show_trailer(self): this function opens the web browser, with the correct URL.
# And the link or the URL, is stored in the instance variable, trailer_youtube_url.
# The way to access this instance variable, is through self.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
