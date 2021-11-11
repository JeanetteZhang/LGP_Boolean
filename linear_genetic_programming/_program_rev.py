from linear_genetic_programming._instruction import Instruction
import copy

from linear_genetic_programming._two_input_boolean_funcs import TwoInputBooleanFuncs


class ProgramRev:
    '''
    A ProgramRev is a collection of instructions. An effective program means all Instruction
    play a role in the return value. The return value goes through a sigmoid function to
    predict class

    Parameters
    ----------

    Attributes
    ----------
    seq : python list
        contain a list of Instructions
    fitness: int
        set after evaluate function, contain calculated fitness
    effProgLen: int
        set after evaluate function, store effective program length

    '''
    OP_AND = 0
    OP_OR = 1
    OP_NAND = 2
    OP_NOR = 3
    OP_EXPON = 4

    def __init__(self):
        self.seq = []

    def makeRandomeProg(self, numberOfOperation, numberOfVariable, numberOfInput, length, regulator = 0):
        ins = Instruction()
        for i in range(length):
            ins.makeRandInstr(numberOfOperation, numberOfVariable, numberOfInput)
            self.seq.append(ins)

    def makeDetermProg(self, instrs, regulator = 0):
        for i in range(len(instrs)):
            self.seq.append(instrs[i])
        self.regulator = regulator

    def toString(self):
        s = ""
        count = 0
        if self.seq == []:
            return "empty program"
        for i in self.seq:
            s += "I" + str(count) + ":  " + i.toString() + "\n"
            count += 1
        return s

    # input is 1 dimension 1 row data
    def execute(self, numberOfVariable, register, input):
        register_copy = copy.deepcopy(register)
        for i in range(len(input)):
            register_copy[i + numberOfVariable] = input[i]
        i = 0
        while i < len(self.seq):
            if self.seq[i].oper_index == self.OP_AND:
                register_copy[self.seq[i].returnRegIndex] = register_copy[self.seq[i].reg1_index] and register_copy[self.seq[i].reg2_index]
            elif self.seq[i].oper_index == self.OP_OR:
                register_copy[self.seq[i].returnRegIndex] = register_copy[self.seq[i].reg1_index] or register_copy[self.seq[i].reg2_index]
            elif self.seq[i].oper_index == self.OP_NAND:
                register_copy[self.seq[i].returnRegIndex] = not (register_copy[self.seq[i].reg1_index] and register_copy[self.seq[i].reg2_index])
            elif self.seq[i].oper_index == self.OP_NOR:  # protected operation
                register_copy[self.seq[i].returnRegIndex] = not (register_copy[self.seq[i].reg1_index] or register_copy[self.seq[i].reg2_index])
            i += 1
        return register_copy[0]

    def eliminateStrcIntron(self):
        strucIntronFreeProg = ProgramRev()
        effInstr = []
        effReg = []
        effReg.append(0)
        i = len(self.seq) - 1
        while i >= 0:
            if self.seq[i].returnRegIndex in effReg:
                if not (self.seq[i].reg1_index in effReg):
                    effReg.append(self.seq[i].reg1_index)
                if not (self.seq[i].reg2_index in effReg):
                    effReg.append(self.seq[i].reg2_index)
                if (self.seq[i].returnRegIndex != self.seq[i].reg1_index) and \
                        (self.seq[i].returnRegIndex != self.seq[i].reg2_index):  # irrelevant
                    effReg.remove(self.seq[i].returnRegIndex)
                effInstr.insert(0, i)
            i -= 1
        for i in range(len(effInstr)):
            strucIntronFreeProg.seq.append(self.seq[effInstr[i]])
        return strucIntronFreeProg

    def get_geno_robust(self):
        neutral_neibor_count = 0
        neibors = TwoInputBooleanFuncs.generateOneStepNeibors(self)
        neibor_pheno = []
        prog_func = TwoInputBooleanFuncs.phenotype(self)
        for i in range(len(neibors)):
            neibor_pheno += [TwoInputBooleanFuncs.phenotype(neibors[i])]
        for j in range(len(neibors)):
            if neibor_pheno[j] == prog_func:
                neutral_neibor_count += 1
        self.robust = neutral_neibor_count

    def get_geno_evolva(self):
        neibor_non_neutral_func = []
        neibors = TwoInputBooleanFuncs.generateOneStepNeibors(self)
        neibor_pheno = []
        prog_func = TwoInputBooleanFuncs.phenotype(self)
        for i in range(len(neibors)):
            neibor_pheno += [TwoInputBooleanFuncs.phenotype(neibors[i])]
        for j in range(len(neibors)):
            if (neibor_pheno[j] != prog_func) and (neibor_pheno[j] not in neibor_non_neutral_func):
                neibor_non_neutral_func += [neibor_pheno[j]]
        self.evolva = len(neibor_non_neutral_func)

    def get_length(self):
        return len(self.seq)
