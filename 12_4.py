import logging
import unittest
from runner import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            obj = Runner('1', -10)
            if obj.speed < 0:
                raise ValueError

            for i in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" прошел успешно')
        except ValueError as exc:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            obj = Runner({1: 'aaa', 2: '52454'})
            if type(obj.name) is not str:
                raise TypeError
            for i in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info('"test_run" прошел успешно')
        except TypeError as exc:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        obj1 = Runner('3')
        obj2 = Runner('4')
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)
