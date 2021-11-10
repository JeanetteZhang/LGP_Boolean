from linear_genetic_programming._program import Program
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
class EnumeratorForRandomWalk:
    RANDOM_WALK_STEP = 10000
    TARGET_PHENO = 0

if __name__ == "__main__":
    prog = Program()
    for i in range(10000):
        prog.makeRandomeProg(4, 2, 2, 4)
        pheno_cur = TwoInputBooleanFuncs.phenotype(prog)
        for j in range(EnumeratorForRandomWalk.RANDOM_WALK_STEP):
            prog_update = TwoInputBooleanFuncs.one_step_mutation(prog)

