import media            #media file contains class definition of Movie
import fresh_tomatoes   #fresh_tomatoes.py file contains open_movies_page function used to create html file

dodgeball = media.Movie("Dodgeball",
                        "https://az616578.vo.msecnd.net/files/responsive/cover/main/desktop/2016/08/21/636074048726998131436357571_dodgeball.jpg",
                        "http://www.pastposters.com/cw3/assets/product_full/R/dodgeball-cinema-quad-movie-poster-(teaser-2).jpg",
                        "https://www.youtube.com/watch?v=W-XbDZUnUmw")          #create dodgeball object

napoleon_dynamite = media.Movie("Napoleon Dynamite",
                        "https://az616578.vo.msecnd.net/files/responsive/cover/main/desktop/2016/03/11/6359326647185971841926479363_Napoleon-Dynamite.jpg",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=qH-FBPRf7NQ")          #create napoleon_dynamite object


movies = [dodgeball, napoleon_dynamite]         #create array with name of Movie objects

fresh_tomatoes.open_movies_page(movies)         #pass array of Movie objects to open_movies_page function 
