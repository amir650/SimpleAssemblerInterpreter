class AssemblyInterpreter:

    def __init__(self):
        self.registers = {}
        self.program_counter = 0
        self.instructions = {
            'mov' : self.moveInstruction,
            'inc' : self.incrementInstruction,
            'dec' : self.decrementInstruction,
            'jnz' : self.jumpNotZeroInstruction
        }

    def lookupRegisterOrValue(self, registerOrValue):
        if registerOrValue in self.registers:
            return self.registers[registerOrValue]
        else:
            return int(registerOrValue)

    def execute(self, program):
        while self.program_counter < len(program) :
            parsed = program[self.program_counter].split()
            current_instruction = parsed[0]
            args = parsed[1:]
            self.program_counter += 1
            self.instructions[current_instruction](*args)

        return self.registers

    def moveInstruction(self, firstOperand, secondOperand):
        self.registers[firstOperand] = self.lookupRegisterOrValue(secondOperand)

    def incrementInstruction(self, x):
        self.registers[x] += 1

    def decrementInstruction(self, x):
        self.registers[x] -= 1

    def jumpNotZeroInstruction(self, x, y):
        if self.lookupRegisterOrValue(x) != 0:
            self.program_counter += self.lookupRegisterOrValue(y) - 1
        pass

def simple_assembler(program):
    return AssemblyInterpreter().execute(program)