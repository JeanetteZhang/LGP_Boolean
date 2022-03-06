from unittest import TestCase, mock

from linear_genetic_programming._program import Program


class TestProg(TestCase):

    def setUp(self) -> None:
        mocked_random_choice = lambda x: 0
        with mock.patch('numpy.random.randint', mocked_random_choice):
            self.prog = Program()
            self.prog.makeRandomeProg(4, 2, 2, 4)

    def test_random_prog(self) -> None:
        self.assertEqual(str(self.prog), "I0:  <AND, r0, r0, r0>\nI1:  <AND, r0, r0, r0>\nI2:  <AND, r0, r0, r0>\nI3:  <AND, r0, r0, r0>\n")

    def test_execute(self):
        # while all the registers are False and the inputs are True
        self.assertEqual(self.prog.execute(2, [False, False, False, False], [True, True]), False)
        self.assertNotEqual(self.prog.execute(2, [False, False, False, False], [True, True]), True)

        # while all the registers are True and the inputs are False
        self.assertEqual(self.prog.execute(2, [True, True, True, True], [False, False]), True)
        self.assertNotEqual(self.prog.execute(2, [True, True, True, True], [False, False]), False)

    def test_fitness(self):
        self.assertEqual(self.prog.fitness(1), 3)