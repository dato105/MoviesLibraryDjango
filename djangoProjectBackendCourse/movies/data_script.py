from library.models import Movie

movies_data = [
    {
        "title": "Inception",
        "description": "A mind-bending thriller about dream invasion.",
        "director": "Christopher Nolan",
        "four_main_actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
        "year_of_release": 2010,
        "poster": ""
    },
    {
        "title": "The Matrix",
        "description": "A hacker discovers the true nature of reality.",
        "director": "Lana Wachowski, Lilly Wachowski",
        "four_main_actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving",
        "year_of_release": 1999,
        "poster": ""
    },

    {
        "title": "Interstellar",
        "description": "Exploring space to save humanity.",
        "director": "Christopher Nolan",
        "four_main_actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine",
        "year_of_release": 2014,
        "poster": ""
    },
    {
        "title": "Parasite",
        "description": "A dark comedy about class conflict.",
        "director": "Bong Joon-ho",
        "four_main_actors": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik",
        "year_of_release": 2019,
        "poster": ""
    },
    {
        "title": "Titanic",
        "description": "Romance set against the tragic sinking of the Titanic.",
        "director": "James Cameron",
        "four_main_actors": "Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates",
        "year_of_release": 1997,
        "poster": ""
    },
    {
        "title": "The Godfather",
        "description": "An organized crime dynasty's rise and fall.",
        "director": "Francis Ford Coppola",
        "four_main_actors": "Marlon Brando, Al Pacino, James Caan, Diane Keaton",
        "year_of_release": 1972,
        "poster": ""
    },
    {
        "title": "Pulp Fiction",
        "description": "Intersecting stories of crime and redemption.",
        "director": "Quentin Tarantino",
        "four_main_actors": "John Travolta, Uma Thurman, Samuel L. Jackson, Bruce Willis",
        "year_of_release": 1994,
        "poster": ""
    },
    {
        "title": "Avatar",
        "description": "A journey to the alien world Pandora.",
        "director": "James Cameron",
        "four_main_actors": "Sam Worthington, Zoe Saldana, Stephen Lang, Sigourney Weaver",
        "year_of_release": 2009,
        "poster": ""
    },
    {
        "title": "The Dark Knight",
        "description": "Batman faces the Joker.",
        "director": "Christopher Nolan",
        "four_main_actors": "Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine",
        "year_of_release": 2008,
        "poster": ""
    },
    {
        "title": "Forrest Gump",
        "description": "A man’s extraordinary life story.",
        "director": "Robert Zemeckis",
        "four_main_actors": "Tom Hanks, Robin Wright, Gary Sinise, Sally Field",
        "year_of_release": 1994,
        "poster": ""
    }
]


for movie in movies_data:
    m = Movie(
        title=movie['title'],
        description=movie['description'],
        director=movie['director'],
        four_main_actors=movie['four_main_actors'],
        year_of_release=movie['year_of_release'])
    m.save()

