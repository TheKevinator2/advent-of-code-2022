from enum import Enum


class Operation(Enum):
    NOOP = 1
    ADDX = 2


def parse_input(file_name):
    program = []
    with open(file_name, 'r') as f:
        for line in f:
            line_op = line.rsplit()
            if 'noop' in line_op:
                operation = (Operation.NOOP, 0)
            if 'addx' in line_op:
                operation = (Operation.ADDX, int(line_op[1]))
            program.append(operation)
    return program


class CPU:
    def __init__(self, program):
        self.register = 1
        self.program = program

    def execute_program(self, n):
        operations = self.get_operations_for_cycle(n)
        register = self.execute_operations(operations)
        self.reset()
        return register

    def get_operations_for_cycle(self, n):
        operations = []
        needed_cycles = 1
        for operation in self.program:
            cycles = operation[0].value
            if needed_cycles + cycles > n:
                break
            operations.append(operation)
            needed_cycles += cycles
        return operations

    def execute_operations(self, operations):
        for operation in operations:
            self.execute_operation(operation)
        return self.register

    def execute_operation(self, operation):
        if operation[0] == Operation.NOOP:
            return
        if operation[0] == Operation.ADDX:
            self.register += operation[1]
            return

    def reset(self):
        self.register = 1


def sum_signal_strengths(file_name):
    program = parse_input(file_name)
    cpu = CPU(program)
    signal_strengths = []
    for cycle in [20, 60, 100, 140, 180, 220]:
        register_value = cpu.execute_program(cycle)
        signal_strength = register_value * cycle
        signal_strengths.append(signal_strength)
    return sum(signal_strengths)


def solve_1(file_name):
    result = sum_signal_strengths(file_name)
    return result


result1 = solve_1("../input.txt")
print(result1)
