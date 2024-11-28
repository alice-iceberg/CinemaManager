import unittest
from datetime import timedelta

from src.movie import Movie
from src.utils import today


class TestMovie(unittest.TestCase):
    def test_prices(self):
        movie = Movie("Title", ["Genre"], 5.0, 10.0, today() + timedelta(days=8))
        self.assertEqual(movie.get_ticket_price(False), 10.0)
        self.assertEqual(movie.get_ticket_price(True), 12.0)

        # Case when the movie is in high\low demand, and ticket is bought 4 days before screening
        movie = Movie("Title", ["Genre"], 5.0, 10.0, today() + timedelta(days=4))
        self.assertEqual(movie.get_ticket_price(True), 13.2)
        self.assertEqual(movie.get_ticket_price(False), 11.0)

        # Case when the movie is in low/high demand, and ticket is bought 31 days before screening
        movie = Movie("Title", ["Genre"], 5.0, 10.0, today() + timedelta(days=31))
        self.assertEqual(movie.get_ticket_price(False), 9.0)
        self.assertEqual(movie.get_ticket_price(True), 10.8)

    def test_number_of_breaks(self):
        movie = Movie("Title", ["Thriller"], 180.0, 10.0, today())
        self.assertEqual(movie.get_number_of_breaks(), 0)

        movie = Movie("Title", ["Comedy"], 200.0, 10.0, today())
        self.assertEqual(movie.get_number_of_breaks(), 2)

        movie = Movie("Title", ["Fantasy"], 45.0, 10.0, today())
        self.assertEqual(movie.get_number_of_breaks(), -1)

        movie = Movie("Title", ["Drama"], 90.0, 10.0, today())
        self.assertEqual(movie.get_number_of_breaks(), 2)

    def test_break_time(self):
        movie = Movie("Title", ["Comedy"], 100.0, 10.0, today())
        self.assertListEqual(movie.get_break_times(), [50.0])

        movie = Movie("Title", ["Fantasy"], 60.0, 10.0, today())
        with self.assertRaises(ValueError):
            movie.get_break_times()

    def test_negative_duration(self):
        with self.assertRaises(ValueError):
            Movie("Title", ["Comedy"], -100.0, 10.0, today())

    def test_negative_base_price(self):
        with self.assertRaises(ValueError):
            Movie("Title", ["Comedy"], 100.0, -10.0, today())


if __name__ == '__main__':
    unittest.main()
