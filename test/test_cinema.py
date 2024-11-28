import unittest
from datetime import timedelta

from src.utils import today
from src.cinema import Cinema
from src.movie import Movie



class CinemaTest(unittest.TestCase):

    def test_cinema_initialization(self):
        number_of_halls = 5

        cinema = Cinema(number_of_halls)
        self.assertEqual(cinema.get_number_of_halls(), number_of_halls)

    def test_cinema_initialization_invalid(self):
        """Test initialization of cinema with zero or negative halls."""
        with self.assertRaises(ValueError):
            Cinema(0)
        with self.assertRaises(ValueError):
            Cinema(-1)

    def test_expand_cinema(self):
        initial_number_of_halls = 5
        number_of_halls_to_add = 3

        cinema = Cinema(initial_number_of_halls)
        cinema.expand_cinema(number_of_halls_to_add)

        self.assertEqual(cinema.get_number_of_halls(), initial_number_of_halls + number_of_halls_to_add)

        # Test expanding with a negative number of halls (should raise ValueError)
        with self.assertRaises(ValueError):
            cinema.expand_cinema(-6)

        # Test expanding with 0 halls
        with self.assertRaises(ValueError):
            cinema.expand_cinema(0)


    def test_get_currently_playing_movies(self):
        cinema = Cinema(5)
        self.assertListEqual(cinema.get_currently_playing_movies(), [])

        # Test when movies are playing
        movie1 = Movie("Test Movie1", ["Genre"], 100.0, 10.0, today() + timedelta(days=3))
        movie2 = Movie("Test Movie2", ["Genre"], 100.0, 10.0, today() - timedelta(days=3))
        hall1 = cinema.halls[0]
        hall2 = cinema.halls[1]

        hall1.plan_screening(movie1, today()+timedelta(days=5))
        hall2.plan_screening(movie2, today()-timedelta(days=1))

        currently_playing = cinema.get_currently_playing_movies()
        self.assertCountEqual(currently_playing, ["Test Movie1"])

    def test_get_number_of_halls(self):
        # Test to ensure the correct number of halls is returned
        cinema = Cinema(3)
        self.assertEqual(cinema.get_number_of_halls(), 3)

        # Test after expanding the cinema
        cinema.expand_cinema(2)
        self.assertEqual(cinema.get_number_of_halls(), 5)

if __name__ == '__main__':
    unittest.main()
