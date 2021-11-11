import copy

from linear_genetic_programming._program import Program
from linear_genetic_programming._genetic_operations import GeneticOperations
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs

class EnumeratorForEdges:

    N_PHENO = 16
    pheno_connects = [[0] * N_PHENO] * N_PHENO

    def generateOneStepNeiborsWithConnections(self, prog):
        neibors = []
        for i in range(prog.get_length()):
            operations = []
            return_reg = []
            reg1 = []
            reg2 = []
            for j in range(GeneticOperations.N_OPERATION):
                operations.append(j)
            operations = list(filter((prog.seq[i].oper_index).__ne__, operations))
            for j in range(GeneticOperations.N_VARIABLE):
                return_reg.append(j)
            return_reg = list(filter((prog.seq[i].returnRegIndex).__ne__, return_reg))
            for j in range(GeneticOperations.N_INPUT + GeneticOperations.N_VARIABLE):
                reg1.append(j)
                reg2.append(j)
            reg1 = list(filter((prog.seq[i].reg1_index).__ne__, reg1))
            reg2 = list(filter((prog.seq[i].reg2_index).__ne__, reg2))
            for m in range(GeneticOperations.N_INSTRUCTION_ONESTEPMUT):
                mutProg = copy.deepcopy(prog)
                if m < GeneticOperations.N_OPERATION - 1:  # mutate operation
                    mutProg.seq[i].oper_index = operations[m]
                elif m - (
                        GeneticOperations.N_OPERATION - 1) < GeneticOperations.N_VARIABLE - 1:  # mutate return register
                    mutProg.seq[i].returnRegIndex = return_reg[m - (GeneticOperations.N_OPERATION - 1)]
                elif m - (
                        GeneticOperations.N_OPERATION - 1 + GeneticOperations.N_VARIABLE - 1) < GeneticOperations.N_VARIABLE + GeneticOperations.N_INPUT - 1:  # mutate calculation register1
                    mutProg.seq[i].reg1_index = reg1[
                        m - (GeneticOperations.N_OPERATION - 1 + GeneticOperations.N_VARIABLE - 1)]
                else:  # mutate calculation register 2
                    mutProg.seq[i].reg2_index = reg2[m - (
                            GeneticOperations.N_OPERATION - 1 + GeneticOperations.N_VARIABLE - 1 + GeneticOperations.N_VARIABLE + GeneticOperations.N_INPUT - 1)]
                neibors.append(mutProg)
                self.pheno_connects[TwoInputBooleanFuncs.phenotype(prog)][TwoInputBooleanFuncs.phenotype(mutProg)] += 1
                self.pheno_connects[TwoInputBooleanFuncs.phenotype(mutProg)][TwoInputBooleanFuncs.phenotype(prog)] += 1

    if __name__ == '__main__':
        f1 = open("pheno_matrix.txt", "w+")
        f2 = open("pheno_edges.txt", "w+")
        instructions = TwoInputBooleanFuncs.generateInstructions()
        num_of_instr = len(instructions)
        
        f1.write("phenotype\t")
        for i in range(16):
            f1.write("%d\t" % i)
        f2.write("pheno1\tpheno2\tweight")

        for i in range(N_PHENO):
            for j in range(N_PHENO):
                pheno_connects[i][j] = pheno_connects[j][i] = 0

        for i in range(num_of_instr):
            for j in range(num_of_instr):
                for k in range(num_of_instr):
                    for l in range(num_of_instr):
                        instrs = []
                        instrs.append(instructions[i])
                        instrs.append(instructions[j])
                        instrs.append(instructions[k])
                        instrs.append(instructions[l])

                        prog = Program()
                        prog.makeDetermProg(instrs)

        for i in range(N_PHENO):
            f1.write(str(i) + "\t")
            for j in range(N_PHENO):
                f1.write(str(pheno_connects[i][j]) + "\t")

        for i in range(N_PHENO):
            for j in range(N_PHENO):
                if pheno_connects[i][j] > 0:
                    f2.write(str(i) + "\t" + str(j) + "\t" + pheno_connects[i][j] / 2)
