from typing import List

from src.hall import Hall


class Cinema:
    def __init__(self, number_of_halls: int):
        if number_of_halls <= 0:
            raise ValueError("number_of_halls must be positive")

        self.halls: List[Hall] = []
        for i in range(number_of_halls):
            self.halls.append(Hall(i, 100))

    def expand_cinema(self, number_of_halls_to_add: int):

        if number_of_halls_to_add <= 0:
            raise ValueError("Number of halls to add must be more than zero.")

        highest_hall_number = max([hall.hall_number for hall in self.halls])
        for i in range(highest_hall_number + 1, highest_hall_number + 1 + number_of_halls_to_add):
            self.halls.append(Hall(i, 100))

    def get_currently_playing_movies(self) -> List[str]:
        currently_playing_movies = set()

        for hall in self.halls:
            upcoming_screenings = hall.get_upcoming_screenings()
            for screening in upcoming_screenings:
                movie = screening.movie
                currently_playing_movies.add(movie.title)

        return list(currently_playing_movies)

    def get_number_of_halls(self):
        return len(self.halls)
