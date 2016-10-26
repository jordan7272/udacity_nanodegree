import media
import fresh_tomatoes

dodgeball = media.Movie("Dodgeball", "https://az616578.vo.msecnd.net/files/responsive/cover/main/desktop/2016/08/21/636074048726998131436357571_dodgeball.jpg", "http://www.pastposters.com/cw3/assets/product_full/R/dodgeball-cinema-quad-movie-poster-(teaser-2).jpg", "https://www.youtube.com/watch?v=W-XbDZUnUmw")

movies = [dodgeball]

fresh_tomatoes.open_movies_page(movies)