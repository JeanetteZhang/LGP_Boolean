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
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                while visited[TwoInputBooleanFuncs.phenotype(prog_update)] and TwoInputBooleanFuncs.phenotype(
                        prog_update) != TwoInputBooleanFuncs.phenotype(prog_cur):
                    prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncs.phenotype(prog_update) == target_pheno:
                    res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                    find = True
                    break
                prog_cur = prog_update
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
        ns = NoveltySearch()
        res[i] = ns.get_dict(i)
    print(NoveltySearch.get_avg(res))

'''
{(7, 3): 34, (12, 1): 26, (11, 11): 0, (7, 12): 44, (14, 4): 55, (13, 4): 139, (12, 12): 0, (0, 7): 20, (15, 1): 16, (0, 10): 12, (3, 7): 16, (2, 5): 98, (1, 11): 43, (8, 5): 55, (5, 8): 31, (4, 0): 134, (10, 8): 9, (9, 0): 2285, (6, 7): 2355, (5, 5): 0, (11, 5): 79, (10, 7): 27, (6, 10): 2500, (15, 11): 5, (14, 1): 55, (13, 7): 86, (0, 4): 3, (15, 4): 10, (1, 1): 0, (8, 15): 57, (4, 10): 103, (3, 2): 9, (9, 14): 2619, (8, 2): 31, (5, 11): 18, (4, 5): 103, (10, 13): 26, (9, 3): 2276, (6, 0): 2279, (11, 0): 98, (7, 5): 30, (14, 15): 35, (12, 11): 26, (15, 14): 8, (14, 2): 53, (13, 10): 104, (0, 1): 11, (3, 12): 24, (1, 12): 53, (8, 12): 44, (4, 15): 102, (3, 1): 14, (2, 11): 78, (5, 14): 26, (10, 14): 12, (6, 13): 2338, (11, 15): 89, (7, 8): 46, (14, 8): 40, (13, 0): 103, (12, 8): 11, (15, 13): 11, (13, 13): 0, (0, 14): 19, (3, 11): 10, (2, 1): 75, (1, 15): 42, (4, 12): 104, (2, 12): 93, (9, 4): 4079, (5, 1): 16, (10, 3): 29, (7, 2): 31, (6, 14): 2644, (12, 2): 28, (11, 10): 67, (7, 15): 46, (14, 5): 49, (13, 3): 81, (12, 13): 7, (15, 0): 16, (1, 5): 46, (0, 11): 12, (2, 2): 0, (1, 10): 50, (4, 1): 103, (9, 7): 2335, (6, 4): 1166, (5, 4): 9, (11, 4): 97, (10, 4): 17, (7, 1): 46, (6, 11): 1555, (12, 7): 26, (15, 10): 13, (14, 6): 1, (0, 5): 12, (15, 7): 14, (1, 0): 50, (0, 8): 16, (4, 11): 83, (3, 5): 24, (2, 7): 114, (9, 13): 1719, (8, 3): 49, (5, 10): 23, (10, 10): 0, (9, 2): 1871, (6, 1): 2513, (5, 7): 11, (11, 3): 95, (7, 4): 44, (14, 12): 28, (12, 4): 12, (14, 3): 47, (0, 2): 5, (3, 15): 28, (1, 3): 40, (8, 13): 45, (4, 8): 86, (3, 0): 26, (2, 8): 70, (9, 8): 2759, (8, 0): 61, (5, 13): 14, (10, 15): 23, (6, 2): 2589, (11, 14): 58, (7, 11): 26, (15, 12): 13, (13, 12): 91, (0, 15): 13, (3, 10): 31, (1, 14): 48, (8, 10): 34, (4, 13): 105, (2, 13): 78, (9, 11): 1546, (5, 0): 27, (10, 0): 29, (6, 15): 2295, (12, 3): 24, (11, 13): 78, (7, 14): 35, (14, 10): 36, (13, 2): 89, (12, 14): 10, (15, 3): 12, (13, 15): 80, (1, 4): 20, (0, 12): 13, (3, 9): 18, (2, 3): 112, (8, 7): 53, (4, 2): 149, (2, 14): 101, (6, 5): 2291, (5, 3): 28, (11, 7): 68, (10, 5): 24, (7, 0): 53, (6, 8): 2306, (12, 0): 26, (11, 8): 82, (7, 13): 43, (14, 7): 48, (13, 5): 100, (1, 7): 54, (3, 4): 16, (2, 4): 76, (9, 12): 2538, (8, 4): 29, (4, 7): 125, (10, 11): 14, (9, 1): 2532, (6, 6): 0, (11, 2): 108, (7, 7): 0, (14, 13): 41, (12, 5): 27, (15, 8): 21, (14, 0): 55, (13, 8): 96, (0, 3): 13, (15, 5): 18, (3, 14): 27, (1, 2): 50, (8, 14): 49, (3, 3): 0, (9, 15): 1945, (8, 1): 42, (5, 12): 32, (4, 4): 0, (10, 12): 25, (6, 3): 2295, (11, 1): 89, (7, 10): 46, (14, 14): 0, (12, 10): 23, (15, 15): 0, (13, 11): 66, (0, 0): 0, (3, 13): 23, (1, 13): 53, (8, 11): 33, (4, 14): 123, (2, 10): 100, (9, 10): 1902, (5, 15): 23, (10, 1): 27, (6, 12): 2717, (11, 12): 86, (14, 11): 35, (13, 1): 77, (12, 15): 21, (15, 2): 12, (13, 14): 96, (0, 13): 15, (3, 8): 25, (2, 0): 114, (1, 8): 36, (8, 8): 0, (4, 3): 105, (2, 15): 104, (9, 5): 2266, (5, 2): 22, (10, 2): 15}
'''
