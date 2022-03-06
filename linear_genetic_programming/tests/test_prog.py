from unittest import TestCase, mock

from linear_genetic_programming._program import Program
from linear_genetic_programming.tests.mock_random import make_mock_random


class TestProg(TestCase):

    def setUp(self) -> None:
        with mock.patch('numpy.random.randint', make_mock_random([0,1,2,3,1,0,2,3,1,1,2,3,0,0,1,2])):
            self.prog = Program.makeRandomeProg(4, 2, 2, 4)

    def test_random_prog(self) -> None:
        self.assertEqual(str(self.prog), (
            "I0:  <NAND, r3, r0, r1>\n"
            "I1:  <NAND, r3, r1, r0>\n"
            "I2:  <NAND, r3, r1, r1>\n"
            "I3:  <OR, r2, r0, r0>\n"
        ))

    def test_execute(self):
        # while all the registers are False and the inputs are True
        self.assertEqual(self.prog.execute(2, [False, False, False, False], [True, True]), False)
        self.assertNotEqual(self.prog.execute(2, [False, False, False, False], [True, True]), True)

        # while all the registers are True and the inputs are False
        self.assertEqual(self.prog.execute(2, [True, True, True, True], [False, False]), True)
        self.assertNotEqual(self.prog.execute(2, [True, True, True, True], [False, False]), False)

    def test_robust(self):
        self.assertEqual(self.prog.get_geno_robust(), 37)

    def test_evolva(self):
        self.assertEqual(self.prog.get_geno_evolva(), 1)

    def test_fitness(self):
        self.assertEqual(self.prog.fitness(1), 3)