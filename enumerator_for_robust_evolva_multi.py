from linear_genetic_programming._program_multi import ProgramMulti
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs_multi import TwoInputBooleanFuncsMulti


class EnumeratorForRobust:
    FUNCLASS = 6

if __name__ == '__main__':
    f1 = open("geno_rob_evolva.txt", "w+")
    f2 = open("geno_rob_evolva_binned.txt", "w+")
    f3 = open("function_classes.txt", "w+")

    instructions = TwoInputBooleanFuncsMulti.generateInstructions()
    num_of_instr = len(instructions)

    geno_mut_robust = []
    geno_evolva = []
    fun_class = []

    for i in range(num_of_instr):
        for j in range(num_of_instr):
            for k in range(num_of_instr):
                for l in range(num_of_instr):
                    instrs = []
                    instrs.append(instructions[i])
                    instrs.append(instructions[j])
                    instrs.append(instructions[k])
                    instrs.append(instructions[l])

                    prog1 = ProgramMulti()
                    prog1.makeDetermProg(instrs, 0)

                    function_class1 = TwoInputBooleanFuncsMulti.phenotype(prog1)
                    fun_class.append(function_class1)

                    prog2 = ProgramMulti()
                    prog2.makeDetermProg(instrs, 1)

                    function_class2 = TwoInputBooleanFuncsMulti.phenotype(prog2)
                    fun_class.append(function_class2)

                    if function_class1 == EnumeratorForRobust.FUNCLASS:
                        prog1.get_geno_robust()
                        robust = prog1.robust
                        geno_mut_robust.append(robust)
                        prog1.get_geno_evolva()
                        evolva = prog1.evolva
                        geno_evolva.append(evolva)
                        f1.write(str(robust) + "\t" + str(evolva))

                    elif function_class2 == EnumeratorForRobust.FUNCLASS:
                        prog2.get_geno_robust()
                        robust = prog2.robust
                        geno_mut_robust.append(robust)
                        prog2.get_geno_evolva()
                        evolva = prog2.evolva
                        geno_evolva.append(evolva)
                        f1.write(str(robust) + "\t" + str(evolva))


    res = Statistics.result(fun_class)
    for p in range(len(res[0])):
        f3.write(str(res[0][p]) + "\t" + str(res[1][p]) + "\n")

    print(str(EnumeratorForRobust.FUNCLASS) + "\t" + str(Statistics.mean(geno_mut_robust)) + "\t" + str(
        Statistics.sd(geno_mut_robust)) + "\t" + str(Statistics.mean(geno_evolva)) + "\t" + str(
        Statistics.sd(geno_evolva)))

    f1.close()
    f2.close()
    f3.close()