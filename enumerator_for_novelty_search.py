import copy

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program import Program
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class NoveltySearch:
    RANDOM_WALK_STEP = 100
    def get_dict(self, target_pheno):
        res_dict = {}
        for i in range(100):
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
            while j < self.RANDOM_WALK_STEP and not find:
                neibors = TwoInputBooleanFuncs.generateOneStepNeibors(prog_cur)
                m = 0
                while m < len(neibors):
                    if TwoInputBooleanFuncs.phenotype(neibors[m]) == target_pheno:
                        res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                        find = True
                        break
                    if visited[TwoInputBooleanFuncs.phenotype(neibors[m])]:
                        m += 1
                    else:
                        j += 1
                        prog_cur = neibors[m]
                        break
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
    print(ns.get_avg(res))
