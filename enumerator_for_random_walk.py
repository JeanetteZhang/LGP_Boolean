import copy

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program_multi import ProgramMulti
from linear_genetic_programming._program_rev import ProgramRev
from linear_genetic_programming._program import Program
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
from linear_genetic_programming._two_input_boolean_funcs_new import TwoInputBooleanFuncsNew
class EnumeratorForRandomWalk:
    RANDOM_WALK_STEP = 10000
    def get_dict(self, target_pheno):
        res_dict_conv = {}
        res_dict_rev = {}
        res_dict_multi = {}
        for i in range(100):
            sequence = []
            for m in range(4):
                instr = Instruction()
                instr.makeRandInstr(4, 2, 2)
                sequence.append(instr)
            
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

            prog_rev = ProgramRev()
            prog_rev.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog_rev)
            prog_update = copy.deepcopy(prog_rev)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_update)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_rev[pheno_cur] = res_dict_rev.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict_rev.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]


            prog_multi = ProgramMulti()
            prog_multi.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog_multi)
            prog_update = copy.deepcopy(prog_rev)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_update)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_multi[pheno_cur] = res_dict_multi.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict_multi.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]

        return res_dict_conv, res_dict_rev, res_dict_multi

if __name__ == "__main__":
    final_dict_conv = {}
    final_dict_rev = {}
    final_dict_multi = {}
    for i in range(16):
        print(i)
        random_walk = EnumeratorForRandomWalk()
        final_dict_conv[i] = random_walk.get_dict(i)[0]
        final_dict_rev[i] = random_walk.get_dict(i)[1]
        final_dict_multi[i] = random_walk.get_dict(2)
    print(final_dict_conv)
    print(final_dict_rev)
    print(final_dict_multi)
