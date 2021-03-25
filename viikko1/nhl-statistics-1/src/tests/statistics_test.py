import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_true_player(self):
        self.statistics.search("Gretzky")
        self.assertTrue(self.statistics.search, "Gretzky")
    
    def test_search_null_player(self):
        self.statistics.search("Gretzkies")
        self.assertTrue(self.statistics.search, None)
    
    def test_top_scorer(self):
        self.statistics.top_scorers(1)
        self.assertTrue(self.statistics.top_scorers, "Yzerman")

    def test_true_team(self):
        self.statistics.team("EDM")
        self.assertTrue(self.statistics, "EDM")

    def test_none_team(self):
        self.statistics.team("EDMI")
        self.assertTrue(self.statistics, None)


    