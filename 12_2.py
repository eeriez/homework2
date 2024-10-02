from runner import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(cls.all_results[key])

    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        result1 = tournament1.start()

        self.assertTrue(result1[max(result1.keys())] == 'Ник')
        self.all_results[1] = result1

    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        result2 = tournament2.start()

        self.assertTrue(result2[max(result2.keys())] == 'Ник')
        self.all_results[2] = result2

    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = tournament3.start()

        self.assertTrue(result3[max(result3.keys())] == 'Ник')
        self.all_results[3] = result3
