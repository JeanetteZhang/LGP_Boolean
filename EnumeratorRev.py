import copy
import time

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program_rev import ProgramRev
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs_new import TwoInputBooleanFuncsNew
class ER:
    RANDOM_WALK_STEP = 1000
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
            prog_con = ProgramRev()
            prog_con.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog_con)
            prog_update = copy.deepcopy(prog_con)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_update)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_conv[pheno_cur] = res_dict_conv.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict_conv.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time1 += end - start

            start = time.time()
            prog2 = ProgramRev()
            prog2.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog2)
            prog_cur = copy.deepcopy(prog2)
            find = False
            visited[pheno_cur] = True
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                while visited[TwoInputBooleanFuncsNew.phenotype(prog_update)] and TwoInputBooleanFuncsNew.phenotype(
                        prog_update) != TwoInputBooleanFuncsNew.phenotype(prog_cur):
                    prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_nove[pheno_cur] = res_dict_nove.get(pheno_cur, []) + [j]
                    find = True
                    break
                prog_cur = prog_update
            if not find:
                res_dict_nove.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time2 += end - start


            start = time.time()
            prog3 = ProgramRev()
            prog3.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog3)
            prog_cur = copy.deepcopy(prog3)
            find = False
            j = 0
            while j < self.RANDOM_WALK_STEP:
                neibor = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                while neibor.fitness(target_pheno) < prog_cur.fitness(target_pheno):
                    neibor = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncsNew.phenotype(neibor) == target_pheno:
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
        hill_climbing = ER()
        res_ran[i] = hill_climbing.get_dict(i)[0]
        res_nove[i] = hill_climbing.get_dict(i)[1]
        res_hill[i] = hill_climbing.get_dict(i)[2]
        time_ran += hill_climbing.get_dict(i)[3]
        time_nove += hill_climbing.get_dict(i)[4]
        time_hill += hill_climbing.get_dict(i)[5]

    print(ER.get_avg(res_ran))
    print(time_ran)
    print(ER.get_avg(res_nove))
    print(time_nove)
    print(ER.get_avg(res_hill))
    print(time_hill)

'''
{(7, 3): 67, (12, 1): 48, (11, 11): 71, (7, 12): 70, (14, 4): 32, (13, 4): 123, (12, 12): 12, (0, 7): 30, (15, 1): 31, (0, 10): 18, (3, 7): 36, (2, 5): 190, (1, 11): 55, (8, 5): 63, (5, 8): 36, (4, 0): 149, (10, 8): 40, (9, 0): 4687, (6, 7): 3981, (5, 5): 12, (11, 5): 147, (10, 7): 42, (6, 10): 3810, (15, 11): 15, (14, 1): 75, (13, 7): 154, (0, 4): 11, (15, 4): 16, (1, 1): 24, (8, 15): 67, (4, 10): 129, (3, 2): 20, (2, 6): 38, (9, 14): 4648, (8, 2): 62, (5, 11): 51, (4, 5): 122, (10, 13): 40, (9, 3): 4804, (6, 0): 3969, (11, 0): 165, (7, 5): 64, (14, 15): 63, (12, 11): 40, (15, 14): 19, (14, 2): 119, (13, 10): 150, (0, 1): 19, (3, 12): 37, (1, 12): 60, (8, 12): 67, (4, 15): 155, (3, 1): 43, (2, 11): 232, (5, 14): 38, (10, 14): 36, (6, 13): 4072, (11, 15): 151, (7, 8): 70, (14, 8): 57, (13, 0): 143, (12, 8): 32, (15, 13): 7, (13, 13): 14, (0, 14): 24, (3, 11): 43, (2, 1): 182, (1, 15): 76, (4, 12): 158, (2, 12): 188, (9, 4): 4420, (5, 1): 33, (10, 3): 48, (7, 2): 53, (6, 14): 3857, (12, 2): 27, (11, 10): 177, (7, 15): 73, (14, 5): 58, (13, 3): 166, (12, 13): 23, (15, 0): 23, (1, 5): 58, (0, 11): 13, (2, 2): 37, (1, 10): 76, (4, 1): 163, (9, 7): 4484, (6, 4): 3132, (5, 4): 14, (11, 4): 177, (10, 4): 28, (7, 1): 51, (6, 11): 4116, (12, 7): 35, (15, 10): 18, (0, 5): 13, (15, 7): 22, (1, 0): 65, (0, 8): 18, (4, 11): 123, (3, 5): 44, (2, 7): 163, (9, 13): 5248, (8, 3): 70, (5, 10): 41, (10, 10): 8, (9, 2): 4041, (6, 1): 4283, (5, 7): 32, (11, 3): 146, (7, 4): 69, (14, 12): 58, (12, 4): 28, (14, 3): 65, (0, 2): 2, (3, 15): 45, (1, 3): 65, (8, 13): 93, (4, 8): 200, (3, 0): 39, (2, 8): 191, (9, 8): 4710, (8, 0): 71, (5, 13): 37, (10, 15): 39, (6, 2): 4665, (11, 14): 149, (7, 11): 47, (15, 12): 20, (13, 12): 155, (0, 15): 17, (3, 10): 43, (1, 14): 81, (8, 10): 67, (4, 13): 170, (2, 13): 124, (9, 11): 3229, (5, 0): 33, (10, 0): 43, (6, 15): 4305, (12, 3): 39, (11, 13): 128, (7, 14): 81, (14, 10): 73, (13, 2): 129, (12, 14): 26, (15, 3): 26, (13, 15): 165, (1, 4): 54, (0, 12): 21, (2, 3): 144, (8, 7): 59, (4, 2): 232, (2, 14): 193, (6, 5): 4124, (5, 3): 43, (11, 7): 130, (10, 5): 37, (7, 0): 71, (6, 8): 5391, (12, 0): 39, (11, 8): 156, (7, 13): 74, (14, 7): 61, (13, 5): 155, (0, 6): 43, (1, 7): 82, (3, 4): 44, (2, 4): 123, (9, 12): 4252, (8, 4): 58, (4, 7): 138, (10, 11): 43, (9, 1): 3209, (11, 2): 211, (7, 7): 37, (14, 13): 37, (12, 5): 44, (15, 8): 26, (14, 0): 73, (13, 8): 164, (0, 3): 14, (15, 5): 25, (3, 14): 44, (1, 2): 51, (8, 14): 77, (4, 9): 15, (3, 3): 10, (9, 15): 3776, (8, 1): 69, (5, 12): 46, (4, 4): 85, (10, 12): 45, (6, 3): 3628, (11, 1): 172, (7, 10): 89, (14, 14): 22, (12, 10): 45, (15, 15): 3, (13, 11): 182, (0, 0): 2, (3, 13): 45, (1, 13): 48, (8, 11): 66, (4, 14): 180, (2, 10): 149, (9, 10): 4008, (5, 15): 42, (10, 1): 45, (6, 12): 4015, (11, 12): 139, (14, 11): 45, (13, 1): 187, (12, 15): 33, (15, 2): 15, (13, 14): 92, (0, 13): 22, (3, 8): 40, (2, 0): 151, (1, 8): 63, (8, 8): 23, (4, 3): 189, (2, 15): 159, (9, 5): 3670, (5, 2): 48, (11, 6): 56, (10, 2): 26}
1735.73900747
{(7, 3): 69, (12, 1): 39, (11, 11): 0, (7, 12): 49, (14, 4): 57, (13, 4): 99, (12, 12): 0, (0, 7): 22, (15, 1): 26, (0, 10): 17, (3, 7): 41, (2, 5): 144, (1, 11): 82, (8, 5): 63, (5, 8): 34, (4, 0): 147, (10, 8): 45, (9, 0): 3806, (6, 7): 4277, (5, 5): 0, (11, 5): 115, (10, 7): 29, (7, 6): 15, (6, 10): 4216, (15, 11): 16, (14, 1): 62, (13, 7): 126, (0, 4): 23, (15, 4): 24, (1, 1): 0, (8, 15): 65, (4, 10): 139, (3, 2): 25, (9, 14): 4142, (8, 2): 76, (5, 11): 57, (4, 5): 164, (10, 13): 35, (9, 3): 5236, (6, 0): 4235, (11, 0): 112, (7, 5): 79, (14, 15): 62, (12, 11): 50, (15, 14): 16, (14, 2): 36, (13, 10): 147, (0, 1): 12, (3, 12): 39, (1, 12): 70, (8, 12): 78, (4, 15): 141, (3, 1): 29, (2, 11): 157, (5, 14): 42, (10, 14): 29, (6, 13): 5365, (11, 15): 157, (7, 8): 60, (14, 8): 51, (13, 0): 127, (12, 8): 33, (15, 13): 11, (13, 13): 0, (0, 14): 18, (3, 11): 31, (2, 1): 164, (1, 15): 61, (4, 12): 154, (2, 12): 149, (9, 4): 3347, (5, 1): 35, (10, 3): 43, (7, 2): 101, (6, 14): 4198, (12, 2): 56, (11, 10): 148, (7, 15): 62, (14, 5): 58, (13, 3): 132, (12, 13): 24, (15, 0): 23, (1, 5): 66, (0, 11): 19, (2, 2): 0, (1, 10): 63, (4, 1): 160, (9, 7): 4891, (6, 4): 4655, (5, 4): 26, (11, 4): 193, (10, 4): 43, (7, 1): 71, (6, 11): 2853, (12, 7): 46, (15, 10): 21, (0, 5): 18, (15, 7): 18, (1, 0): 64, (0, 8): 19, (4, 11): 178, (3, 5): 39, (2, 7): 111, (9, 13): 3891, (8, 3): 62, (5, 10): 38, (10, 10): 0, (9, 2): 3791, (6, 1): 3664, (5, 7): 36, (11, 3): 125, (7, 4): 49, (14, 12): 57, (12, 4): 19, (14, 3): 66, (0, 2): 14, (3, 15): 39, (1, 3): 80, (8, 13): 58, (4, 8): 146, (3, 0): 39, (2, 8): 131, (9, 8): 2956, (8, 0): 64, (5, 13): 26, (10, 15): 35, (6, 2): 4594, (11, 14): 155, (7, 11): 55, (15, 12): 21, (13, 12): 114, (0, 15): 18, (3, 10): 42, (1, 14): 68, (8, 10): 82, (4, 13): 147, (2, 13): 176, (9, 11): 3522, (5, 0): 38, (10, 0): 39, (6, 15): 4594, (12, 3): 40, (11, 13): 139, (7, 14): 50, (14, 10): 68, (13, 2): 129, (12, 14): 29, (15, 3): 17, (13, 15): 157, (1, 4): 44, (0, 12): 17, (2, 3): 184, (8, 7): 69, (4, 2): 199, (2, 14): 141, (9, 6): 3225, (6, 5): 4608, (5, 3): 52, (11, 7): 167, (10, 5): 32, (7, 0): 60, (6, 8): 3889, (12, 0): 35, (11, 8): 146, (7, 13): 77, (14, 7): 74, (13, 5): 132, (1, 7): 75, (3, 4): 33, (2, 4): 117, (9, 12): 4424, (8, 4): 62, (4, 7): 150, (10, 11): 39, (9, 1): 4180, (11, 2): 108, (7, 7): 0, (14, 13): 82, (12, 5): 36, (15, 8): 23, (14, 0): 53, (13, 8): 201, (0, 3): 15, (15, 5): 20, (3, 14): 45, (1, 2): 75, (8, 14): 73, (4, 9): 3, (3, 3): 0, (9, 15): 4152, (8, 1): 61, (5, 12): 38, (4, 4): 0, (10, 12): 42, (6, 3): 4103, (11, 1): 165, (7, 10): 63, (14, 14): 0, (12, 10): 37, (15, 15): 0, (13, 11): 130, (0, 0): 0, (3, 13): 31, (1, 13): 63, (8, 11): 67, (4, 14): 153, (2, 10): 169, (9, 10): 4574, (5, 15): 39, (10, 1): 38, (6, 12): 4150, (11, 12): 138, (14, 11): 73, (13, 1): 155, (12, 15): 37, (15, 2): 19, (13, 14): 167, (0, 13): 16, (3, 8): 30, (2, 0): 165, (1, 8): 68, (8, 8): 0, (4, 3): 141, (2, 15): 116, (9, 5): 4359, (5, 2): 40, (10, 2): 43}
2945.4199543
{(7, 3): 34, (12, 1): 31, (11, 11): 0, (7, 12): 46, (14, 4): 39, (13, 4): 84, (12, 12): 0, (0, 7): 22, (15, 1): 21, (0, 10): 14, (3, 7): 13, (2, 5): 120, (1, 11): 48, (8, 5): 48, (5, 8): 24, (4, 0): 107, (10, 8): 15, (9, 0): 2650, (6, 7): 2608, (5, 5): 0, (11, 5): 83, (10, 7): 25, (6, 10): 2353, (15, 11): 5, (14, 1): 55, (13, 7): 72, (0, 4): 6, (15, 4): 20, (1, 1): 0, (8, 15): 46, (4, 10): 100, (3, 2): 10, (9, 14): 2845, (8, 2): 18, (5, 11): 25, (4, 5): 100, (10, 13): 19, (9, 3): 2509, (6, 0): 2390, (11, 0): 97, (7, 5): 30, (14, 15): 36, (12, 11): 19, (15, 14): 10, (14, 2): 42, (13, 10): 84, (0, 1): 10, (3, 12): 24, (1, 12): 56, (8, 12): 39, (4, 15): 101, (3, 1): 17, (2, 11): 112, (5, 14): 23, (10, 14): 13, (6, 13): 1341, (11, 15): 85, (7, 8): 41, (14, 8): 48, (13, 0): 95, (12, 8): 10, (15, 13): 9, (13, 13): 0, (0, 14): 16, (3, 11): 9, (2, 1): 97, (1, 15): 55, (4, 12): 98, (2, 12): 122, (9, 4): 2846, (5, 1): 10, (10, 3): 29, (7, 2): 57, (6, 14): 2420, (12, 2): 21, (11, 10): 84, (7, 15): 46, (14, 5): 45, (13, 3): 105, (12, 13): 7, (15, 0): 17, (1, 5): 38, (0, 11): 9, (2, 2): 0, (1, 10): 51, (4, 1): 82, (9, 7): 2719, (6, 4): 3318, (5, 4): 11, (11, 4): 127, (10, 4): 24, (7, 1): 40, (6, 11): 2750, (12, 7): 25, (11, 9): 0, (15, 10): 12, (0, 5): 11, (15, 7): 15, (1, 0): 52, (0, 8): 12, (4, 11): 104, (3, 5): 27, (2, 7): 150, (9, 13): 2495, (8, 3): 44, (5, 10): 23, (10, 10): 0, (9, 2): 1237, (6, 1): 2245, (5, 7): 12, (11, 3): 75, (7, 4): 23, (14, 12): 39, (12, 4): 8, (14, 3): 43, (0, 2): 2, (3, 15): 21, (1, 3): 44, (8, 13): 49, (4, 8): 76, (3, 0): 30, (2, 8): 67, (9, 8): 1810, (8, 0): 51, (5, 13): 16, (10, 15): 26, (6, 2): 2628, (11, 14): 79, (7, 11): 26, (15, 12): 14, (13, 12): 70, (0, 15): 14, (3, 10): 32, (1, 14): 49, (8, 10): 35, (4, 13): 147, (2, 13): 125, (9, 11): 3220, (5, 0): 28, (10, 0): 26, (6, 15): 2275, (12, 3): 19, (11, 13): 137, (7, 14): 41, (14, 10): 36, (13, 2): 86, (12, 14): 13, (15, 3): 15, (13, 15): 88, (1, 4): 31, (0, 12): 12, (2, 3): 127, (8, 7): 63, (4, 2): 87, (2, 14): 87, (6, 5): 2018, (5, 3): 27, (11, 7): 93, (10, 5): 26, (7, 0): 46, (6, 8): 2373, (12, 0): 31, (11, 8): 81, (7, 13): 38, (14, 7): 38, (13, 5): 82, (1, 7): 45, (3, 4): 24, (2, 4): 35, (9, 12): 2983, (8, 4): 32, (4, 7): 103, (10, 11): 12, (9, 1): 2070, (11, 2): 108, (7, 7): 0, (14, 13): 37, (12, 5): 28, (15, 8): 17, (14, 0): 49, (13, 8): 90, (0, 3): 10, (15, 5): 15, (3, 14): 20, (1, 2): 36, (8, 14): 50, (3, 3): 0, (9, 15): 2002, (8, 1): 54, (5, 12): 28, (4, 4): 0, (10, 12): 29, (6, 3): 2330, (11, 1): 81, (7, 10): 42, (14, 14): 0, (12, 10): 31, (15, 15): 0, (13, 11): 91, (0, 0): 0, (3, 13): 25, (1, 13): 37, (8, 11): 30, (4, 14): 114, (2, 10): 84, (9, 10): 2223, (5, 15): 25, (10, 1): 30, (6, 12): 2327, (11, 12): 93, (14, 11): 25, (13, 1): 88, (12, 15): 25, (15, 2): 10, (13, 14): 73, (0, 13): 15, (3, 8): 22, (2, 0): 137, (1, 8): 46, (8, 8): 0, (4, 3): 101, (2, 15): 113, (9, 5): 2261, (5, 2): 29, (10, 2): 11}
1661.21697235
'''
