from unittest import TestCase, mock

from linear_genetic_programming._program import Program
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
from linear_genetic_programming.tests.mock_random import make_mock_random


class TestTwoInputs(TestCase):
    def setUp(self) -> None:
        with mock.patch('numpy.random.randint', make_mock_random([0, 1, 2, 3, 1, 0, 2, 3, 1, 1, 2, 3, 0, 0, 1, 2])):
            self.prog = Program.makeRandomeProg(4, 2, 2, 4)

    def test_phenotypes(self):
        self.assertEqual(TwoInputBooleanFuncs.phenotype(self.prog), 0)
        self.assertNotEqual(TwoInputBooleanFuncs.phenotype(self.prog), 1)

    def test_generate_neibor(self):
        self.assertEqual(len(TwoInputBooleanFuncs.generateOneStepNeibors(self.prog)), 40)
        self.assertIsInstance(TwoInputBooleanFuncs.generateOneStepNeibors(self.prog)[0], Program)

    def test_one_neibor(self):
        self.assertIsInstance(TwoInputBooleanFuncs.one_step_mutation(self.prog), Program)