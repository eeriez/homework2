from runner import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(cls.all_results[key])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        result1 = tournament1.start()

        self.assertTrue(result1[max(result1.keys())] == 'Ник')
        self.all_results[1] = result1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        result2 = tournament2.start()

        self.assertTrue(result2[max(result2.keys())] == 'Ник')
        self.all_results[2] = result2

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = tournament3.start()

        self.assertTrue(result3[max(result3.keys())] == 'Ник')
        self.all_results[3] = result3


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        obj = Runner('1')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        obj = Runner('2')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        obj1 = Runner('3')
        obj2 = Runner('4')
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)
