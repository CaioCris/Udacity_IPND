import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club", "https://9to5toys.files.wordpress.com/2015/06/fight-club-poster.jpg?quality=82&strip=all", "https://www.youtube.com/watch?v=SUXWAEX2jlg","David Fincher", "Jim Uhls", "September 10, 1999")

django = media.Movie("Django Unchained", "http://www.djangounchained.org/wp-content/gallery/official-posters/django-unchained-final-american-movie-poster.jpg", "https://www.youtube.com/watch?v=eUdM9vrCbow", "Quentin Tarantino", "Quentin Tarantino", "December 11, 2012")

trainspotting = media.Movie("Trainspotting", "http://www.film4.com/media/images/Channel4/Film4/1990s/T/Trainspotting-Poster.jpg", "https://www.youtube.com/watch?v=nBKWnAdmJJ8", "Danny Boyle", "John Hodge", " February 23, 1996")

the_departed = media.Movie("The Departed", "http://static.rogerebert.com/uploads/movie/movie_poster/the-departed-2007/large_tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg", "https://www.youtube.com/watch?v=SGWvwjZ0eDc", "Martin Scorsese", "William Monahan", "September 26, 2006")

city_of_god = media.Movie("City of God", "http://cdn.miramax.com/media/assets/City-of-God1.png", "https://www.youtube.com/watch?v=ioUE_5wpg_E", "Fernando Meirelles", "Bráulio Mantovani", "August 30, 2002")

pineapple_express = media.Movie("Pineapple Express", "http://www.gstatic.com/tv/thumb/movieposters/176350/p176350_p_v8_ao.jpg", "https://www.youtube.com/watch?v=BWZt4v6b1hI", "David Gordon Green", "Seth Rogen and Evan Goldberg", "August 6, 2008")

movies = [fight_club, django, trainspotting, the_departed, city_of_god, pineapple_express]

fresh_tomatoes.open_movies_page(movies)
