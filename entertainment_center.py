import media
import fresh_tomatoes

# build instances of several movies with title, description,
# poster url and trailer youtube url.
VENOM = media.Movie(
    "VENOM",
    "One of Marvel's most enigmatic, complex and badass characters"
    " comes to the big screen, starring Academy Award nominated ac"
    "tor Tom Hardy as the lethal protector Venom.",
    "https://scontent-dfw5-1.xx.fbcdn.net/v/t1.0-9/27657379_912740"
    "225557710_5213029288107805436_n.jpg?_nc_cat=0&oh=913369d13cef"
    "616a708c864a1ecf7949&oe=5BBC131E",
    "https://www.youtube.com/watch?v=u9Mv98Gr5pY&t=1s"
)

Deadpool_2 = media.Movie(
    "Deadpool 2",
    "After surviving a near fatal bovine attack, a disfigured cafe"
    "teria chef (Wade Wilson) struggles to fulfill his dream of be"
    "coming Mayberry's hottest bartender while also learning to co"
    "pe with his lost sense of taste. Searching to regain his spic"
    "e for life, as well as a flux capacitor, Wade must battle nin"
    "jas, the yakuza, and a pack of sexually aggressive canines, a"
    "s he journeys around the world to discover the importance of "
    "family, friendship, and flavor - finding a new taste for adve"
    "nture and earning the coveted coffee mug title of World's Bes"
    "t Lover.",
    "https://dx35vtwkllhj9.cloudfront.net/twentiethcenturyfox/dead"
    "pool-2/images/regions/us/onesheet.jpg",
    "https://www.youtube.com/watch?v=20bpjtCbCz0"
)

In_Darkness = media.Movie(
    "In Darkness",
    "In Darkness stars Natalie Dormer (Game of Thrones, The Hunger"
    " Games) who is mesmerising in this sophisticated and enthrall"
    "ing edge-of-your-seat thriller.",
    "https://images.fandango.com/ImageRenderer/200/0/redesign/stat"
    "ic/img/default_poster.png/0/images/masterrepository/Fandango/"
    "210883/InDarkness2018.jpg",
    "https://www.youtube.com/watch?v=lAvHoeClyc4"
)

# put movies instances into movies list.
movies = [VENOM, Deadpool_2, In_Darkness]

# generate HTML page and show movies in the moves list.
# open_movies_page takes a list as input. It will show
# the title, poster in one static website.
# user will get trailer video once clicked on the poster.
fresh_tomatoes.open_movies_page(movies)
