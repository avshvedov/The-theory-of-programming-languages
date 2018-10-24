class auto():
    abc = []
    condition = []
    final_condition = []
    init_condition = None
    delta = []
    current_condition = None

    def __init__(self, set_abc, set_condition, set_final_condition, q0):
        self.abc = set_abc
        self.condition = set_condition
        self.final_condition = set_final_condition
        self.init_condition = q0
        self.current_condition = q0

    def add_delta(self, lst):
        if (lst[0] in self.condition and lst[1] in self.abc and lst[2] in self.condition):
            self.delta.append(lst)
        else:
            print("Error")

    def add_delta_list(self, L):
        for i in L:
            print(i)
            self.add_delta(i)
    
    def work(self, input_str):
        self.current_condition = self.init_condition
        for i in input_str:
            for d in self.delta:
                if self.current_condition == d[0] and i == d[1]:
                    a=self.current_condition
                    self.current_condition = d[2]
                    print(a, i, self.current_condition)
                    break
            else:
                print("Правило не найдено")
                return False
        if self.current_condition in self.final_condition:
            return True
        else:
            return False
a=auto(["0", "1", ".", "+", "-"], ["H", "P", "N", "D", "PB"], "P", "H")
a.add_delta_list([["H", "-", "N"],
            ["H", "+", "N"],
            ["H", "0", "PB"],
            ["H", "1", "PB"],
            ["N", "0", "PB"],
            ["N", "1", "PB"],
            ["PB", "0", "PB"],
            ["PB", "1", "PB"],
            ["PB", ".", "P"],
            ["D", "0", "P"],
            ["D", "1", "P"],
            ["P", "0", "P"],
            ["P", "1", "P"]])
