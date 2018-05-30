import media
import fresh_tomatoes

VENOM = media.Movie("VENOM", 
"One of Marvel's most enigmatic, complex and badass characters comes to the big screen, "
"starring Academy Award nominated actor Tom Hardy as the lethal protector Venom.",
"https://scontent-dfw5-1.xx.fbcdn.net/v/t1.0-9/27657379_912740225557710_5213029288107805436_n.jpg?_nc_cat=0&oh=913369d13cef616a708c864a1ecf7949&oe=5BBC131E",
"https://www.youtube.com/watch?v=u9Mv98Gr5pY&t=1s"
)

Deadpool_2 = media.Movie("Deadpool 2", 
"After surviving a near fatal bovine attack, a disfigured cafeteria "
"chef (Wade Wilson) struggles to fulfill his dream of becoming Mayberry's "
"hottest bartender while also learning to cope with his lost sense of taste. "
"Searching to regain his spice for life, as well as a flux capacitor, Wade must "
"battle ninjas, the yakuza, and a pack of sexually aggressive canines, as he "
"journeys around the world to discover the importance of family, friendship, "
"and flavor - finding a new taste for adventure and earning the coveted coffee mug title of World's Best Lover.",
"https://dx35vtwkllhj9.cloudfront.net/twentiethcenturyfox/deadpool-2/images/regions/us/onesheet.jpg",
"https://www.youtube.com/watch?v=20bpjtCbCz0"
)

In_Darkness = media.Movie("In Darkness", 
"In Darkness stars Natalie Dormer (Game of Thrones, The Hunger Games) who "
"is mesmerising in this sophisticated and enthralling edge-of-your-seat thriller.",
"https://images.fandango.com/ImageRenderer/200/0/redesign/static/img/default_poster.png/0/images/masterrepository/Fandango/210883/InDarkness2018.jpg",
"https://www.youtube.com/watch?v=lAvHoeClyc4"
)

movies = [VENOM, Deadpool_2, In_Darkness]           #put movies instances into movies list.

fresh_tomatoes.open_movies_page(movies)             #generate HTML page and show movies in the moves list.
