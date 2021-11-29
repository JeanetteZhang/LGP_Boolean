import copy

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program import Program
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class NoveltySearch:
    RANDOM_WALK_STEP = 10000
    def get_dict(self, target_pheno):
        res_dict = {}
        for i in range(1000):
            visited = [False] * 16
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
            visited[pheno_cur] = True
            j = 0
            while j < self.RANDOM_WALK_STEP:
                neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                while visited[TwoInputBooleanFuncs.phenotype(neibor)] and TwoInputBooleanFuncs.phenotype(neibor) != TwoInputBooleanFuncs.phenotype(prog_cur):
                    neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncs.phenotype(neibor) == target_pheno:
                    res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                    find = True
                    break
                j += 1
                visited[TwoInputBooleanFuncs.phenotype(neibor)] = True
                prog_cur = neibor
            if not find:
                print("yes")
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
        ns = NoveltySearch()
        res[i] = ns.get_dict(i)
    print(NoveltySearch.get_avg(res))

'''
{(0, 0): 0.0, (0, 15): 0.0, (0, 10): 0.5, (1, 1): 0.0, (1, 7): 0.0, (2, 1): 1.0, (2, 8): 1.0, (2, 2): 0.0, (3, 3): 0.0, (3, 12): 1.0, (3, 15): 1.0, (4, 4): 0.0, (4, 5): 0.0, (5, 5): 0.0, (7, 7): 0.0, (7, 11): 1.0, (7, 8): 1.0, (7, 3): 0.0, (8, 8): 0.0, (8, 4): 1.0, (10, 8): 0.0, (10, 0): 0.5, (10, 10): 0.0, (10, 15): 0.0, (11, 11): 0.0, (11, 15): 0.0, (12, 12): 0.0, (12, 0): 0.0, (12, 15): 1.0, (13, 13): 0.0, (13, 14): 1.0, (14, 8): 0.0, (14, 14): 0.0, (14, 1): 1.0, (14, 12): 1.0, (14, 0): 0.0, (15, 0): 1.0, (15, 12): 1.0, (15, 14): 0.0, (15, 15): 0.0, (15, 7): 0.0, (15, 3): 0.0, (15, 10): 1.0, (15, 1): 0.0}
'''