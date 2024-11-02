import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")

    def test_search_none(self):
        result = self.stats.search("Niilo22")
        self.assertEqual(result, None)

    def test_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(result[0].name, "Semenko")
        self.assertEqual(result[2].name, "Gretzky")

    def test_top(self):
        result = self.stats.top(3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_points(self):
        result = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_goals(self):
        result = self.stats.top(5, SortBy.GOALS)
        self.assertEqual(result[0].name, "Lemieux")
        self.assertEqual(result[4].name, "Semenko")

    def test_top_assists(self):
        result = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_invalid(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, "SortBy.GOALS") 