import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = Runner('1')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = Runner('2')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj1 = Runner('3')
        obj2 = Runner('4')
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertEqual(obj1.distance != obj2.distance, True)
