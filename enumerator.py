import copy
import time

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program import Program
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class HC:
    RANDOM_WALK_STEP = 10
    def get_dict(self, target_pheno):
        res_dict_conv = {}
        res_dict_nove = {}
        res_dict_hill = {}
        time1 = 0
        time2 = 0
        time3 = 0
        for i in range(10):
            visited = [False] * 16
            sequence = []
            for m in range(4):
                instr = Instruction()
                instr.makeRandInstr(4, 2, 2)
                sequence.append(instr)

            start = time.time()
            prog_con = Program()
            prog_con.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncs.phenotype(prog_con)
            prog_update = copy.deepcopy(prog_con)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_update)
                if TwoInputBooleanFuncs.phenotype(prog_update) == target_pheno:
                    res_dict_conv[pheno_cur] = res_dict_conv.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict_conv.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time1 += end - start

            start = time.time()
            prog2 = Program()
            prog2.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncs.phenotype(prog2)
            prog_cur = copy.deepcopy(prog2)
            find = False
            visited[pheno_cur] = True
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                while visited[TwoInputBooleanFuncs.phenotype(prog_update)] and TwoInputBooleanFuncs.phenotype(
                        prog_update) != TwoInputBooleanFuncs.phenotype(prog_cur):
                    prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncs.phenotype(prog_update) == target_pheno:
                    res_dict_nove[pheno_cur] = res_dict_nove.get(pheno_cur, []) + [j]
                    find = True
                    break
                prog_cur = prog_update
            if not find:
                res_dict_nove.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time2 += end - start


            start = time.time()
            prog3 = Program()
            prog3.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncs.phenotype(prog3)
            prog_cur = copy.deepcopy(prog3)
            find = False
            j = 0
            while j < self.RANDOM_WALK_STEP:
                neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                while neibor.fitness(target_pheno) < prog_cur.fitness(target_pheno):
                    neibor = TwoInputBooleanFuncs.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncs.phenotype(neibor) == target_pheno:
                    res_dict_hill[pheno_cur] = res_dict_hill.get(pheno_cur, []) + [j]
                    find = True
                    break
                j += 1
                prog_cur = neibor
            if not find:
                res_dict_hill.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time3 += end - start
        return res_dict_conv, res_dict_nove, res_dict_hill, time1, time2, time3

    @staticmethod
    def get_avg(dic):
        avg = {}
        for key1, value1 in dic.items():
            for key2, value2 in value1.items():
                avg[(key1, key2)] = Statistics.mean(value2)
        return avg

if __name__ == "__main__":
    final_dict = {}
    res_ran = {}
    res_hill = {}
    res_nove = {}
    time_ran = 0
    time_nove = 0
    time_hill = 0
    for i in range(16):
        print(i)
        hill_climbing = HC()
        res_ran[i] = hill_climbing.get_dict(i)[0]
        res_nove[i] = hill_climbing.get_dict(i)[1]
        res_hill[i] = hill_climbing.get_dict(i)[2]
        time_ran += hill_climbing.get_dict(i)[3]
        time_nove += hill_climbing.get_dict(i)[4]
        time_hill += hill_climbing.get_dict(i)[5]

    print(HC.get_avg(res_ran))
    print(time_ran)
    print(HC.get_avg(res_nove))
    print(time_nove)
    print(HC.get_avg(res_hill))
    print(time_hill)

'''
{(7, 3): 34, (6, 9): 1071, (12, 1): 29, (11, 11): 0, (7, 12): 37, (14, 4): 39, (13, 4): 74, (12, 12): 0, (0, 7): 14, (15, 1): 23, (0, 10): 12, (3, 7): 11, (2, 5): 112, (1, 11): 37, (8, 5): 51, (5, 8): 24, (4, 0): 112, (10, 8): 13, (9, 0): 2276, (6, 7): 2855, (5, 5): 0, (11, 5): 95, (10, 7): 21, (6, 10): 2424, (15, 11): 5, (14, 1): 41, (13, 7): 79, (0, 4): 11, (15, 4): 11, (1, 1): 0, (8, 15): 57, (4, 10): 103, (3, 2): 13, (9, 14): 2541, (8, 2): 20, (5, 11): 18, (4, 5): 109, (10, 13): 23, (9, 3): 2282, (6, 0): 2313, (11, 0): 109, (7, 5): 40, (14, 15): 35, (12, 11): 21, (15, 14): 12, (14, 2): 39, (13, 10): 63, (0, 1): 9, (3, 12): 25, (1, 12): 48, (8, 12): 44, (4, 15): 120, (3, 1): 15, (2, 11): 127, (5, 14): 27, (10, 14): 10, (6, 13): 2747, (11, 15): 72, (7, 8): 47, (14, 8): 35, (13, 0): 99, (12, 8): 6, (15, 13): 11, (13, 13): 0, (0, 14): 19, (3, 11): 8, (2, 1): 105, (1, 15): 61, (4, 12): 108, (2, 12): 116, (9, 4): 1295, (5, 1): 12, (10, 3): 33, (7, 2): 59, (6, 14): 2488, (12, 2): 22, (11, 10): 88, (7, 15): 45, (14, 5): 43, (13, 3): 87, (12, 13): 10, (15, 0): 18, (1, 5): 45, (0, 11): 14, (2, 2): 0, (1, 10): 49, (4, 1): 119, (9, 7): 1882, (6, 4): 2463, (5, 4): 9, (11, 4): 52, (10, 4): 19, (7, 1): 37, (6, 11): 1592, (12, 7): 26, (15, 10): 11, (0, 5): 11, (15, 7): 12, (1, 0): 52, (0, 8): 12, (4, 11): 87, (3, 5): 27, (2, 7): 133, (9, 13): 1501, (8, 3): 60, (5, 10): 23, (4, 6): 22, (10, 10): 0, (9, 2): 2409, (6, 1): 1983, (5, 7): 11, (11, 3): 93, (7, 4): 32, (14, 12): 40, (12, 4): 11, (14, 3): 46, (0, 2): 5, (3, 15): 28, (1, 3): 40, (8, 13): 33, (4, 8): 83, (3, 0): 28, (2, 8): 106, (9, 8): 2108, (8, 0): 66, (5, 13): 6, (10, 15): 24, (6, 2): 1511, (11, 14): 98, (7, 11): 43, (15, 12): 14, (13, 12): 85, (0, 15): 11, (3, 10): 38, (1, 14): 52, (8, 10): 45, (4, 13): 133, (2, 13): 132, (9, 11): 1345, (5, 0): 28, (10, 0): 28, (6, 15): 2169, (12, 3): 27, (11, 13): 47, (7, 14): 55, (14, 10): 41, (13, 2): 75, (12, 14): 10, (15, 3): 15, (13, 15): 81, (1, 4): 28, (0, 12): 13, (2, 3): 91, (8, 7): 51, (4, 2): 70, (2, 14): 139, (6, 5): 2268, (5, 3): 23, (11, 7): 78, (10, 5): 21, (7, 0): 48, (6, 8): 2351, (12, 0): 28, (11, 8): 103, (7, 13): 27, (14, 7): 37, (13, 5): 90, (1, 7): 46, (3, 4): 19, (2, 4): 76, (9, 12): 2683, (8, 4): 27, (4, 7): 105, (10, 11): 14, (9, 1): 2218, (11, 2): 81, (7, 7): 0, (14, 13): 35, (12, 5): 30, (15, 8): 19, (14, 0): 51, (13, 8): 90, (0, 3): 14, (15, 5): 14, (3, 14): 28, (1, 2): 40, (8, 14): 54, (3, 3): 0, (9, 15): 2572, (8, 1): 47, (5, 12): 35, (4, 4): 0, (10, 12): 29, (6, 3): 2441, (11, 1): 91, (7, 10): 56, (14, 14): 0, (12, 10): 27, (15, 15): 0, (13, 11): 53, (0, 0): 0, (3, 13): 17, (1, 13): 51, (8, 11): 33, (4, 14): 119, (2, 10): 99, (9, 10): 2204, (5, 15): 27, (10, 1): 29, (6, 12): 2271, (11, 12): 86, (14, 11): 50, (13, 1): 110, (12, 15): 21, (15, 2): 14, (13, 14): 76, (0, 13): 10, (3, 8): 29, (2, 0): 122, (1, 8): 34, (8, 8): 0, (4, 3): 113, (2, 15): 100, (9, 5): 2450, (5, 2): 16, (11, 6): 16, (10, 2): 7}
'''
