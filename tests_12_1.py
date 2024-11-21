# Домашнее задание по теме "Простые Юнит-Тесты"
# Задача "Проверка на выносливость"

import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_run(self):
        self.name = 'Фёдор'
        r1 = runner.Runner(self.name)
        for i in range(0, 10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_walk(self):
        self.name = 'Иван'
        r2 = runner.Runner(self.name)
        for i in range(0, 10):
           r2.walk()
        self.assertEqual(r2.distance, 50)

    def test_challenge(self):
        self.name_1 = 'Фёдор'
        self.name_2 = 'Иван'
        r1 = runner.Runner(self.name_1)
        r2 = runner.Runner(self.name_2)
        for i in range(0, 10):
            r2.walk()
            r1.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == "__main__":
    unittest.main()
