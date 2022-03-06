from unittest import TestCase, mock

from linear_genetic_programming._program import Program
from linear_genetic_programming.tests.mock_random import make_mock_random


class TestProg(TestCase):

    def setUp(self) -> None:
        with mock.patch('numpy.random.randint', make_mock_random([3,2,1,0,3,2,0,1,2,3,1,1,2,1,0,0])):
            self.prog = Program.makeRandomeProg(4, 2, 2, 4)

    def test_random_prog(self) -> None:
        self.assertEqual(str(self.prog), (
            "I0:  <OR, r0, r3, r2>\n"
            "I1:  <AND, r1, r3, r2>\n"
            "I2:  <OR, r1, r2, r3>\n"
            "I3:  <AND, r0, r2, r1>\n"
        ))

    def test_execute(self):
        # while all the registers are False and the inputs are True
        self.assertEqual(self.prog.execute(2, [False, False, False, False], [True, True]), True)
        self.assertNotEqual(self.prog.execute(2, [False, False, False, False], [True, True]), False)

        # while all the registers are True and the inputs are False
        self.assertEqual(self.prog.execute(2, [True, True, True, True], [False, False]), False)
        self.assertNotEqual(self.prog.execute(2, [True, True, True, True], [False, False]), True)

    def test_robust(self):
        self.assertEqual(self.prog.get_geno_robust(), 26)

    def test_evolva(self):
        self.assertEqual(self.prog.get_geno_evolva(), 7)

    def test_fitness(self):
        self.assertEqual(self.prog.fitness(1), 3)