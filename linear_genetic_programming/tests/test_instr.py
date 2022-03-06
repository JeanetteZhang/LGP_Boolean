from unittest import TestCase, mock

from linear_genetic_programming._instruction import Instruction

class TestProg(TestCase):
    def test_random_instr_one(self):
        mocked_random_choice = lambda x: 1
        with mock.patch('numpy.random.randint', mocked_random_choice):
            res = str(Instruction.makeRandInstr(4, 2, 2))
        self.assertNotEqual(res, "<OR, r1, r1, r0>")

    def test_random_instr_two(self):
        mocked_random_choice = lambda x: 1
        with mock.patch('numpy.random.randint', mocked_random_choice):
            res = str(Instruction.makeRandInstr(4, 2, 2))
        self.assertEqual(res, "<OR, r1, r1, r1>")