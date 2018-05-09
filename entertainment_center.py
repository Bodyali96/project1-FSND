"""
A module that creates a movies objects
	based on the data passed from media module,
	and then pars them to the HTML page using
	fresh_tomatoes.open_movies_page() method
"""
import media
import fresh_tomatoes


#  Logan: movie title, movie imdb link, storyline, poster image and trailer url
logan = media.Movie("Logan",  # movie title
							"https://www.imdb.com/title/tt3315342/?ref_=nv_sr_1", # movie imdb link
                            "In the near future, a weary Logan cares for "  # storyline
                            "an ailing Professor X, somewhere on the Mexican "
                            "border. However, Logan's attempts to hide from the world, "
                            "and his legacy, are upended when a "
                            "young mutant arrives, pursued by dark forces.",
                            "https://ia.media-imdb.com/images/"  # poster image
                            "M/MV5BYzc5MTU4N2EtYTkyMi00NjdhLTg3NWEt"
                            "MTY4OTEyMzJhZTAzXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=Div0iP65aZo")


#  Interstellar: movie title, movie imdb link, storyline, poster image and trailer url
interstellar  = media.Movie("Interstellar ",  # movie title
							"https://www.imdb.com/title/tt0816692/?ref_=nv_sr_4", # movie imdb link
                            "A team of explorers travel through "  # storyline
                            "a wormhole in space in an "
                            "attempt to ensure humanity's survival.",
                           	"https://ia.media-imdb.com/images/"  # poster image
                           	"M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFm"
                           	"MjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQX"
                           	"VyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=zSWdZVtXT7E")


#  Get Out: movie title, movie imdb link, storyline, poster image and trailer url
get_out = media.Movie("Get Out",  # movie title
							"https://www.imdb.com/title/tt5052448/?ref_=nv_sr_2", # movie imdb link
                            "A young African-American visits his "  # storyline
                            "white girlfriend's parents "
                            "for the weekend, where his simmering "
                            "uneasiness about their reception of "
                            "him eventually reaches a boiling point.",
                            "https://ia.media-imdb.com/images/"  # poster image
                            "M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkF"
                            "tZTgwNzcwMzc0MTI@._V1_SY"
                            "1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=DzfpyUB60YY&t=3s")


#  La La Land: movie title, movie imdb link, storyline, poster image and trailer url
La_La_Land = media.Movie("La La Land",  # movie title
							"https://www.imdb.com/title/tt3783958/?ref_=nv_sr_1", # movie imdb link
                            "While navigating their careers in Los Angeles, "  # storyline
                            "a pianist and an actress fall in love while "
                            "attempting to reconcile "
                            "their aspirations for the future.",
                            "https://ia.media-imdb.com/images/M/"  # poster image
                            "MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgw"
                            "NTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=0pdqf4P9MB8")

#  Avengers: Infinity War: movie title, movie imdb link, storyline, poster image and trailer url
avengers = media.Movie("Avengers: Infinity War",  # movie title
							"https://www.imdb.com/title/tt4154756/?ref_=nv_sr_2", # movie imdb link
                            "The Avengers and their allies must be "  # storyline
                            "willing to sacrifice all in an attempt "
                            "to defeat the powerful Thanos before his "
                            "blitz of devastation and "
                            "ruin puts an end to the universe.",
                            "https://ia.media-imdb.com/images/M"  #poster image
                            "/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZ"
                            "TgwNzY1MTUwNTM@._V1_SY"
                            "1000_CR0,0,674,1000_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=6ZfuNTqbHE8")


#  The Hunger Games: movie title, movie imdb link, storyline, poster image and trailer url
the_hunger_games = media.Movie("The Hunger Games",  # movie title
							"https://www.imdb.com/title/tt1392170/?ref_=nv_sr_2", # movie imdb link
                            "Katniss Everdeen voluntarily takes "  # storyline
                            "her younger sister's place in the "
                            "Hunger Games: a televised competition "
                            "in which two teenagers from each of the "
                            "twelve Districts of Panem are chosen "
                            "at random to fight to the death.",
                            "https://ia.media-imdb.com/images/M"  # poster image
                            "/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZT"
                            "cwNTgyNzkyNw@@._V1_SY"
                            "1000_CR0,0,674,1000_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=mfmrPu43DF8")


#  List of movies that will be parsed to the page using media.py file
movies = [
    logan, interstellar, get_out,
    La_La_Land, avengers, the_hunger_games
    ]


#  Creating the HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
