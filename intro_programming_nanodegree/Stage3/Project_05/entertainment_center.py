import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an alien planet", "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

trainspotting = media.Movie("Trainspotting","Scottishs friends addicted in heroin", "http://www.film4.com/media/images/Channel4/Film4/1990s/T/Trainspotting-Poster.jpg", "https://www.youtube.com/watch?v=nBKWnAdmJJ8")

school_of_rock = media.Movie("School of rock","Jack Black make a rock band with teenager from middle school", "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille","A rat who have cook abilities", "http://www.impawards.com/2007/posters/ratatouille.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_pares = media.Movie("Midnight in paris","a movie with Owen Wilson", "https://natashastander.files.wordpress.com/2014/07/mip.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, trainspotting, school_of_rock, ratatouille, midnight_in_pares]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)