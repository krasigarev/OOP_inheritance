class Computer:
    def __init__(self, pc: str, laptop: str):
        self.pc = pc
        self.laptop = laptop

    def type_computer(self):
        return f"Type is {self.pc} and {self.laptop}"


class Personal_computer(Computer):
    def __init__(self, pc: str, laptop: str, monitor: str, case: str):
        Computer.__init__(self, pc, laptop)
        self.monitor = monitor
        self.case = case


    def my_pc(self):
        return f"This is my pc!!"


class Cpu(Personal_computer):
    def __init__(self, pc: str, laptop: str, monitor: str, case: str, frequency_1: str, name: str):
        Personal_computer.__init__(self, pc, laptop, monitor, case)
        self.frequency = frequency_1
        self.name = name

    def all_pc(self):
        return f"super pc"


a = Cpu("pc: per_kom", 'laptop: dell', 'monitor: HP', 'case: cooler master', 'cpu: frequency: 2600MHz', 'Name: Krasi garev')

print(a.case)
print(a.name)
print(a.pc)
print(a.laptop)
print(a.monitor)
print(a.frequency)
