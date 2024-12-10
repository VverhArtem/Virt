class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.instructions = []
        self.instruction_pointer = 0

    def load_program(self, instructions):
        self.instructions = instructions

    def run(self):
        while self.instruction_pointer < len(self.instructions):
            instruction = self.instructions[self.instruction_pointer]
            self.execute(instruction)
            self.instruction_pointer += 1

    def execute(self, instruction):
        operation = instruction[0]

        if operation == "PUSH":
            value = instruction[1]
            self.stack.append(value)
        elif operation == "POP":
            if self.stack:
                self.stack.pop()
        elif operation == "ADD":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)
        elif operation == "SUB":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a - b)
        elif operation == "PRINT":
            print(self.stack[-1])
        else:
            raise ValueError(f"Неизвестная команда: {operation}")

program = [
    ("PUSH", 10),
    ("PUSH", 20),
    ("ADD",),
    ("PUSH", 5),
    ("SUB",),
    ("PRINT",)
]

vm = VirtualMachine()
vm.load_program(program)
vm.run()
