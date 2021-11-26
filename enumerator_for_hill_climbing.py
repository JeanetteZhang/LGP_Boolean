import copy

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program import Program
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class HillClimbing:
    RANDOM_WALK_STEP = 10000
    def get_dict(self, target_pheno):
        res_dict = {}
        for i in range(10):
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
            while j < self.RANDOM_WALK_STEP and not find:
                neibors = TwoInputBooleanFuncs.generateOneStepNeibors(prog_cur)
                m = 0
                while m < len(neibors):
                    if TwoInputBooleanFuncs.phenotype(neibors[m]) == target_pheno:
                        res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                        find = True
                        break
                    if neibors[m].fitness(target_pheno) < prog_cur.fitness(target_pheno):
                        m += 1
                    else:
                        j += 1
                        prog_cur = neibors[m]
                        break
            if not find:
                res_dict.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
        print(res_dict)
        return res_dict

if __name__ == "main":
    final_dict = {}
    for i in range(16):
        print(i)
        hill_climbing = HillClimbing()
        print(hill_climbing.get_dict(5))
