from linear_genetic_programming._program import Program
from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._genetic_operations import GeneticOperations
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs


class EnumeratorForRobust:
    FUNCLASS = 6

    if __name__ == '__main__':
        f1 = open("geno_rob_evolva.txt", "w+")
        f2 = open("geno_rob_evolva_binned.txt", "w+")
        f3 = open("function_classes.txt", "w+")

        instructions = TwoInputBooleanFuncs.generateInstructions()
        num_of_instr = len(instructions)

        geno_mut_robust = []
        geno_evolva = []
        fun_class = []

        for i in range(1):
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
                        function_class = TwoInputBooleanFuncs.phenotype(prog)
                        fun_class.append(function_class)

                        if function_class == FUNCLASS:
                            prog.get_geno_robust()
                            robust = prog.robust
                            geno_mut_robust.append(robust)
                            prog.get_geno_evolva()
                            evolva = prog.evolva
                            geno_evolva.append(evolva)
                            f1.write(str(robust) + "\t" + str(evolva))
                            print(evolva)


        res = Statistics.result(fun_class)
        for p in range(len(res[0])):
            f3.write(str(res[0][p]) + "\t" + str(res[1][p]) + "\n")

        print(str(FUNCLASS) + "\t" + str(Statistics.mean(geno_mut_robust)) + "\t" + str(
            Statistics.sd(geno_mut_robust)) + "\t" + str(Statistics.mean(geno_evolva)) + "\t" + str(
            Statistics.sd(geno_evolva)))
