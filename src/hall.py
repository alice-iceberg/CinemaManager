from datetime import datetime, timedelta
from typing import Dict, List

from src.movie import Movie
from src.utils import generate_unique_identifier, today


class Screening:
    def __init__(self, movie: Movie, played_at: datetime):
        self.screening_id = generate_unique_identifier()
        self.movie = movie
        self.played_at = played_at
        self.reservations = 0


class Hall:
    def __init__(self, hall_number: int, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self.hall_number = hall_number
        self.capacity = capacity
        self.screenings: Dict[int, Screening] = {}

    def plan_screening(self, movie: Movie, movie_start_time: datetime):
        for _, screening in self.screenings.items():
            screening_start = screening.played_at
            screening_end = screening.played_at + timedelta(minutes=movie.duration + movie.get_number_of_breaks() * 5)

            if screening_start <= movie_start_time <= screening_end:
                raise ValueError("Movie cannot begin when another movie is already playing!")

        if movie_start_time < movie.release_date:
            raise ValueError("Cannot show movie before it is released!")

        screening = Screening(movie, movie_start_time)
        self.screenings[screening.screening_id] = screening
        return screening.screening_id

    def book_tickets(self, screening_id: int, number_of_tickets: int) -> float:
        if screening_id not in self.screenings:
            raise ValueError("Cannot find screening!")

        screening = self.screenings[screening_id]
        if screening.reservations + number_of_tickets > self.capacity:
            raise ValueError("Not enough space for the number of reservations")

        screening.reservations += number_of_tickets
        ticket_price = screening.movie.get_ticket_price(self.capacity - screening.reservations < self.capacity * 0.1)
        return ticket_price * number_of_tickets

    def cancel_screening(self, screening_id: int) -> float:
        if screening_id not in self.screenings:
            raise ValueError("Cannot find screening!")

        screening = self.screenings.pop(screening_id)
        money_to_refund = screening.reservations * screening.movie.get_ticket_price(False)
        return money_to_refund

    def get_upcoming_screenings(self) -> List[Screening]:
        screenings = []
        for _, screening in self.screenings.items():
            if screening.played_at > today():
                screenings.append(screening)

        screenings.sort(key=lambda screening: screening.played_at)
        return screenings
