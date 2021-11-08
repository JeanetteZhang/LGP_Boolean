from linear_genetic_programming._program import Program
from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._genetic_operations import GeneticOperations
test = Program()
ins = Instruction()
ins.makeDetermInstr(2, 0, 3, 2)
test.makeDetermProg([ins])
GeneticOperations.microMutation(test)