# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.name_1 = 'Усэйн'
        self.speed_1 = 10
        self.name_2 = 'Андрей'
        self.speed_2 = 9
        self.name_3 = 'Ник'
        self.speed_3 = 3

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def tearDown(self):
        for i in range(1, len(self.all_results)+1):
            result = self.all_results[i]
            self.assertTrue(result[len(result)] == self.name_3)

    def test_run_1(self):
        self.distance = 90
        r1 = runner_and_tournament.Runner(self.name_1, self.speed_1)
        r3 = runner_and_tournament.Runner(self.name_3, self.speed_3)
        runner_tournament = runner_and_tournament.Tournament(self.distance, r1, r3)
        self.all_results[1]= runner_tournament.start()

    def test_run_2(self):
        self.distance = 90
        r2 = runner_and_tournament.Runner(self.name_2, self.speed_2)
        r3 = runner_and_tournament.Runner(self.name_3, self.speed_3)
        runner_tournament = runner_and_tournament.Tournament(self.distance, r2, r3)
        self.all_results[2] = runner_tournament.start()

    def test_run_3(self):
        self.distance = 90
        r1 = runner_and_tournament.Runner(self.name_1, self.speed_1)
        r2 = runner_and_tournament.Runner(self.name_2, self.speed_2)
        r3 = runner_and_tournament.Runner(self.name_3, self.speed_3)
        runner_tournament = runner_and_tournament.Tournament(self.distance, r1, r2, r3)
        self.all_results[3] = runner_tournament.start()

    @classmethod
    def tearDownClass(cls):
        for i in range(1, len(cls.all_results)+1):
            result_tournament = cls.all_results[i]
            for j in range(1, len(result_tournament)+1):
                result_tournament[j] = result_tournament[j].name
            print(str(result_tournament).replace("'",""))

if __name__ == "__main__":
    unittest.main()
