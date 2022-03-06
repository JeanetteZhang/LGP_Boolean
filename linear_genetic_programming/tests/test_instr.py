from unittest import TestCase, mock

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming.tests.mock_random import make_mock_random


class TestProg(TestCase):
    def test_random_instr_one(self):

        with mock.patch('numpy.random.randint', make_mock_random([0,1,2,3])):
            res = str(Instruction.makeRandInstr(4, 2, 2))
        self.assertNotEqual(res, "<OR, r1, r1, r0>")
        self.assertEqual(res, "<NAND, r3, r0, r1>")

