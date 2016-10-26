import media
import fresh_tomatoes

dodgeball = media.Movie("Dodgeball", 
                        "https://az616578.vo.msecnd.net/files/responsive/cover/main/desktop/2016/08/21/636074048726998131436357571_dodgeball.jpg", 
                        "http://www.pastposters.com/cw3/assets/product_full/R/dodgeball-cinema-quad-movie-poster-(teaser-2).jpg", 
                        "https://www.youtube.com/watch?v=W-XbDZUnUmw")
                        
napoleon_dynamite = media.Movie("Napoleon Dynamite", 
                        "https://az616578.vo.msecnd.net/files/responsive/cover/main/desktop/2016/03/11/6359326647185971841926479363_Napoleon-Dynamite.jpg", 
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_UX182_CR0,0,182,268_AL_.jpg", 
                        "https://www.youtube.com/watch?v=qH-FBPRf7NQ")


movies = [dodgeball, napoleon_dynamite]

fresh_tomatoes.open_movies_page(movies)