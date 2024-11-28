from datetime import datetime

from src.cinema import Cinema
from src.hall import Hall
from src.movie import Movie

if __name__ == "__main__":
    # Declaring new movies
    m1 = Movie("Lord of the Rings: The Two Towers", ["Fantasy"], 179, 130.0, datetime(2002, 12, 18))
    m2 = Movie("Alien", ["Sci-fi", "Thriller"], 116, 150.0, datetime(1979, 11, 2))
    m3 = Movie("Fast & Furious 16", ["Racing"], 148, 110.0, datetime(2023, 11, 15))

    # Declaring a cinema
    cinema = Cinema(4)
    cinema.expand_cinema(2)
    hall = cinema.halls[0]

    # Planning & cancelling movies
    screening_id = hall.plan_movie(m1, datetime(2024, 12, 12))
    print(f"Booked a new screening with id {screening_id}")
    to_refund = hall.cancel_movie(screening_id)
    print(f"Movie cancelled, should refund: {to_refund} SEK")

    # Planning & booking
    screening_id = hall.plan_movie(m2, datetime(2026, 12, 12))
    print(f"Booked a new screening with id {screening_id}")
    price = hall.book_tickets(screening_id, 4)
    print(f"Visitor should pay {price} SEK for their tickets")

    # Switching to another hall
    hall = cinema.halls[1]
    screening_id = hall.plan_movie(m3, datetime(2025, 12, 12))

    # Upcoming movies
    upcoming_screenings_in_hall = hall.get_upcoming_screenings()
    print(f"Screenings that will be played in the hall: {upcoming_screenings_in_hall}")

    movies_playing_in_cinema = cinema.get_currently_playing_movies()
    print(f"Movies that will be played in the cinema: {movies_playing_in_cinema}")
