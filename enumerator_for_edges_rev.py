import copy

from linear_genetic_programming._program_rev import ProgramRev
from linear_genetic_programming._constants import Constants
from linear_genetic_programming._two_input_boolean_funcs_new import TwoInputBooleanFuncsNew


class EnumeratorForEdgesRev:

    N_PHENO = 16
    pheno_connects = [[0] * N_PHENO] * N_PHENO

    def generateOneStepNeiborsWithConnections(self, prog):
        for i in range(prog.get_length()):
            operations = []
            return_reg = []
            reg1 = []
            reg2 = []
            for j in range(Constants.N_OPERATION):
                operations.append(j)
            operations = list(filter((prog.seq[i].oper_index).__ne__, operations))
            for j in range(Constants.N_VARIABLE):
                return_reg.append(j)
            return_reg = list(filter((prog.seq[i].returnRegIndex).__ne__, return_reg))
            for j in range(Constants.N_INPUT + Constants.N_VARIABLE):
                reg1.append(j)
                reg2.append(j)
            reg1 = list(filter((prog.seq[i].reg1_index).__ne__, reg1))
            reg2 = list(filter((prog.seq[i].reg2_index).__ne__, reg2))
            for m in range(Constants.N_INSTRUCTION_ONESTEPMUT):
                mutProg = copy.deepcopy(prog)
                if m < Constants.N_OPERATION - 1:  # mutate operation
                    mutProg.seq[i].oper_index = operations[m]
                elif m - (
                        Constants.N_OPERATION - 1) < Constants.N_VARIABLE - 1:  # mutate return register
                    mutProg.seq[i].returnRegIndex = return_reg[m - (Constants.N_OPERATION - 1)]
                elif m - (
                        Constants.N_OPERATION - 1 + Constants.N_VARIABLE - 1) < Constants.N_VARIABLE + Constants.N_INPUT - 1:  # mutate calculation register1
                    mutProg.seq[i].reg1_index = reg1[
                        m - (Constants.N_OPERATION - 1 + Constants.N_VARIABLE - 1)]
                else:  # mutate calculation register 2
                    mutProg.seq[i].reg2_index = reg2[m - (
                            Constants.N_OPERATION - 1 + Constants.N_VARIABLE - 1 + Constants.N_VARIABLE + Constants.N_INPUT - 1)]
                self.pheno_connects[TwoInputBooleanFuncsNew.phenotype(prog)][TwoInputBooleanFuncsNew.phenotype(mutProg)] += 1
                self.pheno_connects[TwoInputBooleanFuncsNew.phenotype(mutProg)][TwoInputBooleanFuncsNew.phenotype(prog)] += 1
        reg_prog = copy.deepcopy(prog)
        reg_prog.regulator = 1 - prog.regulator
        self.pheno_connects[TwoInputBooleanFuncsNew.phenotype(prog)][TwoInputBooleanFuncsNew.phenotype(reg_prog)] += 1
        self.pheno_connects[TwoInputBooleanFuncsNew.phenotype(reg_prog)][TwoInputBooleanFuncsNew.phenotype(prog)] += 1

if __name__ == '__main__':
    f1 = open("pheno_matrix.txt", "w+")
    f2 = open("pheno_edges.txt", "w+")
    instructions = TwoInputBooleanFuncsNew.generateInstructions()
    num_of_instr = len(instructions)

    f1.write("phenotype\t")
    for i in range(16):
        f1.write("%d\t" % i)
    f2.write("pheno1\tpheno2\tweight\n")

    enumerator = EnumeratorForEdgesRev()
    for i in range(num_of_instr):
        for j in range(num_of_instr):
            for k in range(num_of_instr):
                for l in range(num_of_instr):
                    instrs = []
                    instrs.append(instructions[i])
                    instrs.append(instructions[j])
                    instrs.append(instructions[k])
                    instrs.append(instructions[l])

                    prog1 = ProgramRev()
                    prog1.makeDetermProg(instrs, 0)
                    enumerator.generateOneStepNeiborsWithConnections(prog1)

                    prog2 = ProgramRev()
                    prog2.makeDetermProg(instrs, 1)
                    enumerator.generateOneStepNeiborsWithConnections(prog2)

    for i in range(EnumeratorForEdgesRev.N_PHENO):
        f1.write(str(i) + "\t")
        for j in range(EnumeratorForEdgesRev.N_PHENO):
            f1.write(str(enumerator.pheno_connects[i][j]) + "\t")

    for i in range(EnumeratorForEdgesRev.N_PHENO):
        for j in range(EnumeratorForEdgesRev.N_PHENO):
            if enumerator.pheno_connects[i][j] > 0:
                f2.write(str(i) + "\t" + str(j) + "\t" + str(enumerator.pheno_connects[i][j] / 2) + "\n")
