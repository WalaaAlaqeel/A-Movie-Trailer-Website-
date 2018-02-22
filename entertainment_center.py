import media  # calls the contents of meda.py to define the class Movie.
import fresh_tomatoes  # takes in list of movies and output them in a website

# 1st Movie information
beauty_and_the_beast = media.Movie('Beauty And The Beast',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://youtu.be/OvW_L8sTu5E')


# 2ed  Movie information
bilal = media.Movie('BILAL',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMDE0NzkwNTMtNzQ0MC00ZjFhLTlkNjMtMjA1NzcwOTBjYjZjXkEyXkFqcGdeQXVyMTYxMzQzNTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://youtu.be/Wp_7Gdf2blE')


# 3ed  Movie information
the_young_victoria = media.Movie('The Young Victoria',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4MjExMDk3NV5BMl5BanBnXkFtZTcwMTU3OTMwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://youtu.be/dwoHPrQ5M10')


# 4th  Movie information
home_alone = media.Movie('Home Alone',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMzFkM2YwOTQtYzk2Mi00N2VlLWE3NTItN2YwNDg1YmY0ZDNmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
'https://youtu.be/bAlHIbPvtcw')


# 5th  Movie information
Snowden_files  = media.Movie('The Snowden Files',
'http://t2.gstatic.com/images?q=tbn:ANd9GcT6ubiHoOe0om1-IaC_CV4vgb_j8zR4Voa1vlHnChY1Gb95g2tM',
'https://youtu.be/QlSAiI3xMh4')


# 6th  Movie information
the_intern  = media.Movie('The Intern',
'https://upload.wikimedia.org/wikipedia/ar/8/87/%D9%81%D9%8A%D9%84%D9%85_%D8%A7%D9%84%D9%85%D8%AA%D8%AF%D8%B1%D8%A8.jpg',
'https://youtu.be/ZU3Xban0Y6A')

# movies array: I will use it as input to open_movies_page() function, to displays movies as web page by fresh_tomatoes.py.
movies = [beauty_and_the_beast, bilal, the_young_victoria, home_alone, Snowden_files, the_intern]
fresh_tomatoes.open_movies_page(movies)
