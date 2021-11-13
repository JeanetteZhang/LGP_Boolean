import numpy as np
import copy


class GeneticOperations:
    '''
    GeneticOperations implements crossover and two types of mutation
    '''

    N_OPERATION = 4
    N_INPUT = 2
    N_VARIABLE = 2
    N_INSTRUCTION_ONESTEPMUT = (N_OPERATION - 1) + (N_VARIABLE - 1) + (N_VARIABLE + N_INPUT - 1) + (
                N_VARIABLE + N_INPUT - 1)