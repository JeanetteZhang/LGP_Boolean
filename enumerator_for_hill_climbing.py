import copy

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program import Program
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class HillClimbing:
    RANDOM_WALK_STEP = 10000
    def get_dict(self, target_pheno):
        res_dict = {}
        for i in range(1000):
            sequence = []
            for m in range(4):
                instr = Instruction()
                instr.makeRandInstr(4, 2, 2)
                sequence.append(instr)

            prog = Program()
            prog.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncs.phenotype(prog)
            prog_cur = copy.deepcopy(prog)
            find = False
            j = 0
            while j < self.RANDOM_WALK_STEP:
                neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                while neibor.fitness(target_pheno) < prog_cur.fitness(target_pheno):
                    neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncs.phenotype(neibor) == target_pheno:
                    res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                    find = True
                    break
                j += 1
                prog_cur = neibor
            if not find:
                res_dict.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
        return res_dict

    @staticmethod
    def get_avg(dic):
        avg = {}
        for key1, value1 in dic.items():
            for key2, value2 in value1.items():
                avg[(key1, key2)] = Statistics.mean(value2)
        return avg

if __name__ == "__main__":
    final_dict = {}
    res = {}
    for i in range(16):
        print(i)
        hill_climbing = HillClimbing()
        res[i] = hill_climbing.get_dict(i)
    print(HillClimbing.get_avg(res))

'''
{(0, 15): 0.0, (0, 0): 0.0, (0, 12): 0.5, (0, 8): 0.0, (0, 5): 0.0, (0, 4): 1.0, (0, 10): 0.0, (1, 1): 0.0, (1, 14): 0.0, (1, 7): 0.0, (1, 0): 0.0, (2, 2): 0.0, (3, 3): 0.0, (3, 0): 0.0, (3, 11): 0.0, (4, 4): 0.0, (4, 12): 0.0, (5, 5): 0.0, (5, 7): 0.0, (5, 4): 0.0, (5, 15): 0.0, (5, 1): 0.0, (7, 7): 0.0, (8, 8): 0.0, (10, 10): 0.0, (10, 2): 0.0, (11, 11): 0.0, (11, 10): 0.0, (12, 12): 0.0, (12, 15): 0.0, (12, 4): 0.0, (13, 15): 0.0, (13, 13): 0.0, (14, 0): 0.0, (14, 14): 0.0, (14, 1): 1.0, (15, 15): 0.0, (15, 13): 0.5, (15, 11): 0.0, (15, 14): 0.0, (15, 10): 0.0, (15, 0): 1.0, (15, 5): 0.0}
'''