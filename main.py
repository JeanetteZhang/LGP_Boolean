from linear_genetic_programming._program import Program
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs
if __name__ == '__main__':
    prog = Program()
    prog.makeRandomeProg(4, 2, 2, 4)
    print(TwoInputBooleanFuncs.phenotype(prog))