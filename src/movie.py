from datetime import datetime
from math import floor
from typing import List

from src.utils import days_between_datetimes, today


class Movie:
    def __init__(self, title: str, genres: List[str], duration: float, base_price: float,
                 release_date: datetime):
        if duration <= 0:
            raise ValueError("duration must be positive!")

        if base_price <= 0:
            raise ValueError("base_price must be positive!")

        self.title = title
        self.genres = genres
        self.duration = duration  # In minutes
        self.base_price = base_price
        self.release_date = release_date

    def get_ticket_price(self, in_high_demand: bool) -> float:
        price = self.base_price
        if days_between_datetimes(self.release_date, today()) < 5:
            price += price * 0.1

        if days_between_datetimes(self.release_date, today()) > 30:
            price -= price * 0.1

        if in_high_demand:
            price += price * 0.2

        return price

    def get_number_of_breaks(self) -> int:
        breaks = floor(self.duration / 90.0)
        if "Thriller" in self.genres or "Horror" in self.genres:
            return 0
        if "Sci-fi" in self.genres or "Fantasy" in self.genres:
            return breaks - 1
        if "Romance" in self.genres or "Drama" in self.genres:
            return breaks + 1

        return breaks

    def get_break_times(self) -> List[int]:
        number_of_movie_segments = self.get_number_of_breaks() + 1

        if number_of_movie_segments == 0:
            raise ValueError("Number of movie segments should not be zero")
        movie_segment_lengths = int(self.duration // number_of_movie_segments)

        break_times = []
        for i in range(1, number_of_movie_segments):
            break_times.append(i * movie_segment_lengths)
        return break_times
