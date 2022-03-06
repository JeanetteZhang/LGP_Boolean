# Regulatory Genotype-to-Phenotype Mappings Improve Evolvability in Genetic Programming
Simplifies biological genotype-phenotype mapping to a computational structure,
provides implementation of Boolean linear genetic program(LGP),
and numerically explores the features of programs.

## Example
Each program is fixed to have four lines of instructions.
Each instruction has a return register, two operand registers, and an operator. 
The LGP algorithm in this study operates on Boolean variables and relationships,
therefore, all registers take Boolean values 
and a set of Boolean functions {AND, OR, NAND, NOR} are employed as operators.

We consider a two-input, one-output Boolean LGP algorithm.
The Boolean inputs are stored in registers r2 and r3.
Calculation register r0 is designated as the output register,
and r1 is added as another calculation register.
To prevent over-writing the inputs, 
we specify that only calculation registers can serve as the return in an instruction,
whereas both calculation and input registers can be used as an operand.

A classic LGP program is shown as follows:
```
I0:  <OR, r0, r3, r2>
I1:  <AND, r1, r3, r2>
I2:  <OR, r1, r2, r3>
I3:  <AND, r0, r2, r1>
```

In our LGP algorithm, 
a linear genetic program maps two Boolean variables to one Boolean variable,
i.e., the input is one of the four possible pairs, 
i.e., {{TRUE, TRUE}, {TRUE, FALSE}, {FALSE, TRUE}, {FALSE, FALSE}},
while the output is either TRUE or FALSE.
Thus, there are 2<sup>4</sup> = 16 possible Boolean relationships represented by such linear genetic programs.
Each of these 16 Boolean relationships is defined as a phenotype.

The possible phenotypes are shown as below:
```
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
```

## Development
To install the LGP_Boolean package and run the test cases, you need to run
```
git clone https://github.com/JeanetteZhang/LGP_Boolean.git
bash test.sh
```
LGP_Boolean requires the following software:

- Python 3.4+
- NumPy