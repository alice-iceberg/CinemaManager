import unittest
from datetime import timedelta, datetime

from src.hall import Hall, Screening
from src.movie import Movie
from src.utils import today


class HallTest(unittest.TestCase):

    def test_plan_movie(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))
        first_start_time = today() + timedelta(days=1)

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, first_start_time)
        self.assertIn(screening_id, hall.screenings)

        # Test case when movie_start_time < movie.release_date
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today())
        release_time = today() - timedelta(days=1)
        with self.assertRaises(ValueError):
            screening_id = hall.plan_screening(movie, release_time)

        # Test when movie start time overlaps with an existing screening's time range
        movie = Movie("Test Movie", ["Genre"], 120.0, 10.0, datetime(2024, 1, 1))
        hall = Hall(1, 100)

        # Plan the first screening at 10:00 AM
        first_screening_start = datetime(2024, 1, 1, 10, 0)
        hall.plan_screening(movie, first_screening_start)

        # Plan the second screening that overlaps with the first
        overlapping_start = datetime(2024, 1, 1, 11, 0)  # Starts at 11:00, which overlaps with the first
        with self.assertRaises(ValueError):
            hall.plan_screening(movie, overlapping_start)

    def test_book_tickets(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))
        number_reservations = 10

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, today())
        hall.book_tickets(screening_id, number_reservations)

        self.assertEqual(hall.screenings[screening_id].reservations, number_reservations)

        # Test case when screening id does not exist
        with self.assertRaises(ValueError):
            screening_id = 100
            hall.book_tickets(screening_id, number_reservations)

        # Test case when number of tickets exceeds the capacity
        with self.assertRaises(ValueError):
            number_reservations = 110
            screening_id = hall.plan_screening(movie, today())
            hall.book_tickets(screening_id, number_reservations)

    def test_cancel_screening(self):
        movie = Movie("Test Movie", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))

        hall = Hall(0, 100)
        screening_id = hall.plan_screening(movie, today())
        hall.cancel_screening(screening_id)

        self.assertNotIn(screening_id, hall.screenings)

        # Test case when screening id does not exist
        with self.assertRaises(ValueError):
            screening_id = 100
            hall.cancel_screening(screening_id)

    def test_upcoming_screenings(self):
        movie = Movie("Test Movie1", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))

        hall = Hall(0, 100)
        hall.plan_screening(movie, today() + timedelta(days=1))
        hall.plan_screening(movie, today() + timedelta(days=2))
        hall.plan_screening(movie, today() + timedelta(days=3))

        self.assertEqual(len(hall.get_upcoming_screenings()), 3)

        # Test the case when there are no added screenings
        hall = Hall(2, 100)
        self.assertEqual(len(hall.get_upcoming_screenings()), 0)

    def test_zero_capacity(self):
        with self.assertRaises(ValueError):
            hall = Hall(1, 0)


if __name__ == '__main__':
    unittest.main()
