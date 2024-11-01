import unittest
from statistics_service import StatisticsService
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
        self.assertAlmostEqual(result.name, "Kurri")

    def test_search_none(self):
        result = self.stats.search("Niilo22")
        self.assertAlmostEqual(result, None)

    def test_team(self):
        result = self.stats.team("EDM")
        self.assertAlmostEqual(result[0].name, "Semenko")
        self.assertAlmostEqual(result[2].name, "Gretzky")

    def test_top(self):
        result = self.stats.top(3)
        self.assertAlmostEqual(result[0].name, "Gretzky")
        self.assertAlmostEqual(result[2].name, "Yzerman")