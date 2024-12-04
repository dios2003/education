# Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest
import tests_12_1
import tests_12_2

runnerSt = unittest.TestSuite()
runnerSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runnerSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerSt)
