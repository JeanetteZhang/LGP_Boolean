import copy
import numpy as np

import linear_genetic_programming._constants as _constants
from linear_genetic_programming._instruction import Instruction


class TwoInputBooleanFuncsNew:
    falseFunction = (False, False, False, False)  # 0
    andFunction = (False, False, False, True)  # 1
    notYandXFunction = (False, False, True, False)  # 2
    XFunction = (False, False, True, True)  # 3
    notXandYFunction = (False, True, False, False)  # 4
    YFunction = (False, True, False, True)  # 5
    xorFunction = (False, True, True, False)  # 6
    orFunction = (False, True, True, True)  # 7
    norFunction = (True, False, False, False)  # 8
    equalFunction = (True, False, False, True)  # 9
    notYFunction = (True, False, True, False)  # 10
    XleYFunction = (True, False, True, True)  # 11
    notXFunction = (True, True, False, False)  # 12
    YleXFunction = (True, True, False, True)  # 13
    nandFunction = (True, True, True, False)  # 14
    trueFunction = (True, True, True, True)  # 15

    number_of_samples = (int)(2 ** _constants.N_INPUT)
    sample_inputs = ((False, False), (False, True), (True, False), (True, True))

    phenotypes = (falseFunction,
                  andFunction,
                  notYandXFunction,
                  XFunction,
                  notXandYFunction,
                  YFunction,
                  xorFunction,
                  orFunction,
                  norFunction,
                  equalFunction,
                  notYFunction,
                  XleYFunction,
                  notXFunction,
                  YleXFunction,
                  nandFunction,
                  trueFunction)

    @staticmethod
    def generateInstructions():
        instructions = []
        for i in range(_constants.N_OPERATION):  # 4
            for j in range(_constants.N_VARIABLE):  # 2
                for k in range(_constants.N_VARIABLE + _constants.N_INPUT):  # 2+2
                    for l in range(_constants.N_VARIABLE + _constants.N_INPUT):  # 2+2
                        ins = Instruction()
                        ins.makeDetermInstr(i, j, k, l)
                        instructions.append(ins)
        return instructions

    @staticmethod
    def phenotype(prog):
        classLabel = 0
        registers = []
        for i in range(_constants.N_INPUT + _constants.N_VARIABLE):
            registers.append(False)
        mutProg = copy.copy(prog)
        mutProg.eliminateStrcIntron()

        execute_results = [False] * TwoInputBooleanFuncsNew.number_of_samples
        for j in range(TwoInputBooleanFuncsNew.number_of_samples):
            execute_results[j] = mutProg.execute(_constants.N_VARIABLE, registers,
                                                 TwoInputBooleanFuncsNew.sample_inputs[j])

        for k in range(16):
            if execute_results[0] == TwoInputBooleanFuncsNew.phenotypes[k][0] and execute_results[1] == \
                    TwoInputBooleanFuncsNew.phenotypes[k][1] and execute_results[2] == TwoInputBooleanFuncsNew.phenotypes[k][
                2] and execute_results[3] == TwoInputBooleanFuncsNew.phenotypes[k][3]:
                classLabel = k
        return classLabel

    @staticmethod
    def generateOneStepNeibors(prog):
        neibors = []
        for i in range(prog.get_length()):
            operations = []
            return_reg = []
            reg1 = []
            reg2 = []
            for j in range(_constants.N_OPERATION):
                operations.append(j)
            operations = list(filter(float(prog.seq[i].oper_index).__ne__, operations))
            for j in range(_constants.N_VARIABLE):
                return_reg.append(j)
            return_reg = list(filter(float(prog.seq[i].returnRegIndex).__ne__, return_reg))
            for j in range(_constants.N_INPUT + _constants.N_VARIABLE):
                reg1.append(j)
                reg2.append(j)
            reg1 = list(filter(float(prog.seq[i].reg1_index).__ne__, reg1))
            reg2 = list(filter(float(prog.seq[i].reg2_index).__ne__, reg2))
            for m in range(_constants.N_INSTRUCTION_ONESTEPMUT):
                mutProg = copy.deepcopy(prog)
                if m < _constants.N_OPERATION - 1:  # mutate operation
                    mutProg.seq[i].oper_index = operations[m]
                elif m - (
                        _constants.N_OPERATION - 1) < _constants.N_VARIABLE - 1:  # mutate return register
                    mutProg.seq[i].returnRegIndex = return_reg[m - (_constants.N_OPERATION - 1)]
                elif m - (
                        _constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1) < _constants.N_VARIABLE + _constants.N_INPUT - 1:  # mutate calculation register1
                    mutProg.seq[i].reg1_index = reg1[
                        m - (_constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1)]
                else:  # mutate calculation register 2
                    mutProg.seq[i].reg2_index = reg2[m - (
                            _constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1 + _constants.N_VARIABLE + _constants.N_INPUT - 1)]
                neibors.append(mutProg)
        reg_prog = copy.deepcopy(prog)
        reg_prog.regulator = 1 - prog.regulator
        neibors.append(reg_prog)
        return neibors

    @staticmethod
    def one_step_mutation(prog):
        mutProg = copy.deepcopy(prog)
        operations = []
        return_reg = []
        reg1 = []
        reg2 = []

        i = np.random.randint(prog.get_length())
        m = np.random.randint(_constants.N_INSTRUCTION_ONESTEPMUT + 1)
        if m == _constants.N_INSTRUCTION_ONESTEPMUT:
            reg_prog = copy.deepcopy(prog)
            reg_prog.regulator = 1 - prog.regulator
            return reg_prog

        for j in range(_constants.N_OPERATION):
            operations.append(j)
        operations = list(filter(float(prog.seq[i].oper_index).__ne__, operations))
        for j in range(_constants.N_VARIABLE):
            return_reg.append(j)
        return_reg = list(filter(float(prog.seq[i].returnRegIndex).__ne__, return_reg))
        for j in range(_constants.N_INPUT + _constants.N_VARIABLE):
            reg1.append(j)
            reg2.append(j)
        reg1 = list(filter(float(prog.seq[i].reg1_index).__ne__, reg1))
        reg2 = list(filter(float(prog.seq[i].reg2_index).__ne__, reg2))

        if m < _constants.N_OPERATION - 1:  # mutate operation
            mutProg.seq[i].oper_index = operations[m]
        elif m - (
                _constants.N_OPERATION - 1) < _constants.N_VARIABLE - 1:  # mutate return register
            mutProg.seq[i].returnRegIndex = return_reg[m - (_constants.N_OPERATION - 1)]
        elif m - (
                _constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1) < _constants.N_VARIABLE + _constants.N_INPUT - 1:  # mutate calculation register1
            mutProg.seq[i].reg1_index = reg1[
                m - (_constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1)]
        else:  # mutate calculation register 2
            mutProg.seq[i].reg2_index = reg2[m - (
                    _constants.N_OPERATION - 1 + _constants.N_VARIABLE - 1 + _constants.N_VARIABLE + _constants.N_INPUT - 1)]
        return mutProg
