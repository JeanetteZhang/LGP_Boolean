import numpy as np


class Instruction:
    '''
    Instruction is the lowest level in classification model. It contains a return register,
    an operation and two calculation registers. For example, "r[0] = r[2] NAND r[3]", r[0] is
    a return register, r[1] is a calculation register, r[2] and r[3] are input registers.
    'NAND' is operation register.

    Parameters
    ----------
    numberOfOperation
    numberOfVariable
    numberOfInput
    numberOfConstant

    Attributes
    ----------
    operIndex
        calculated using random number in len(numberOfOperation)
    returnRegIndex
        calculated using random number in len(numberOfVariable)
    reg1_index
    reg2_index

    '''

    # np.random.seed(0)
    OP_AND = 0
    OP_OR = 1
    OP_NAND = 2
    OP_NOR = 3

    def __init__(self):
        pass

    def makeRandInstr(self, numberOfOperation, numberOfVariable, numberOfInput):
        ''' This is a function helps make random instruction. '''
        r1 = np.random.randint(numberOfVariable + numberOfInput)
        self.reg1_index = r1
        r2 = np.random.randint(numberOfVariable + numberOfInput)
        self.reg2_index = r2
        self.oper_index = np.random.randint(numberOfOperation)
        self.returnRegIndex = np.random.randint(numberOfVariable)

    def makeDetermInstr(self, indexOfOperation, indexOfRetReg, indexOfReg1, indexOfReg2):
        ''' This is a function helps make denterm instruction. '''
        self.oper_index, self.returnRegIndex, self.reg1_index, self.reg2_index = \
            indexOfOperation, indexOfRetReg, indexOfReg1, indexOfReg2

    def toString(self):
        s = "<"

        if self.oper_index == self.OP_AND:
            s += "AND"
        elif self.oper_index == self.OP_OR:
            s += "OR"
        elif self.oper_index == self.OP_NAND:
            s += "NAND"
        elif self.oper_index == self.OP_NOR:
            s += "NOR"
        s += ", r" + str(self.returnRegIndex) + ", "
        s += "r" + str(self.reg1_index)
        s += ", "
        s += "r" + str(self.reg2_index)

        s += ">"
        return s
