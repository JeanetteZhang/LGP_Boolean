from linear_genetic_programming._program import Program
from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._genetic_operations import GeneticOperations
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs

class EnumeratorForEdges:

    @staticmethod
    def main():
        f1 = open("pheno_matrix.txt", "w+")
        f2 = open("pheno_edges.txt", "w+")
        instructions = TwoInputBooleanFuncs.generateInstructions()
        num_of_instr = len(instructions)
        
        f1.write("phenotype\t")
        for i in range(16):
            f1.write("%d\t" % i)
        f2.write("pheno1\tpheno2\tweight")
        
        
test = Program()
ins = Instruction()
ins.makeDetermInstr(2, 0, 3, 2)
print(ins.toString())
test.makeDetermProg([ins])
print(test)