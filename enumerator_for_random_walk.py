import copy

from linear_genetic_programming._program import Program
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class EnumeratorForRandomWalk:
    RANDOM_WALK_STEP = 10000
    def get_dict(self, target_pheno):
        res_dict = {}
        for i in range(10000):
            prog = Program()
            prog.makeRandomeProg(4, 2, 2, 4)

            pheno_cur = TwoInputBooleanFuncs.phenotype(prog)
            prog_update = copy.deepcopy(prog)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncs.one_step_mutation(prog_update)
                if TwoInputBooleanFuncs.phenotype(prog_update) == target_pheno:
                    res_dict[pheno_cur] = res_dict.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
        return res_dict

if __name__ == "__main__":
    final_dict = {}
    for i in range(16):
        random_walk = EnumeratorForRandomWalk()
        final_dict[i] = random_walk.get_dict(i)
    print(final_dict)