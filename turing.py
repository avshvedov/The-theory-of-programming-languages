class Head:
    position=None
    state=None

    def __init__(self, p, s):
        self.position = p
        self.state = s

    def change(self, p, s):
        self.position = p
        self.state = s
        
class Turing:
    condition = None
    abc = None
    line = None
    rules = None
    action=["R", "L", "Q"]
    head = None
    
    def __init__(self, n):
        self.head = Head(0, "S0")
        self.abc=[]
        self.line=[]
        self.rules=[]
        self.condition=["S0","Q"]
        for i in range(n): 
            self.line.append(" ")
            
    def print_line(self):
        s="".join(self.line)
        print(s)
        
    def print_head(self, n):
        s=""
        for i in range(len(self.line)):
            if i==n:
                s+="^"
            else:
                s+=" "
        print(s)
        
    def add_abc(self, a):
        self.abc.append(a)

    def add_condition(self, c):
        self.condition.append(c)

    def add_rules(self, r):
        if r[0] in self.abc and r[1] in self.condition and r[2] in self.abc and r[3] in self.condition and r[4] in self.action:
            self.rules.append(r)
        else:
            print("Error")

        
    def add_text(self, text):
        j = 1
        for i in text:
            if i in self.abc:
                self.line[j] = i
                j+=1
            else:
                print("Error")
                break

    def work(self):
        while (self.head.state != "Q"):
            for i in self.rules:
                if self.line[self.head.position]==i[0] and self.head.state == i[1]:
                    
                    self.print_line()
                    self.print_head(self.head.position)
                    
                    self.line[self.head.position] = i[2]
                    self.head.state = i[3]
                    
                    if i[4]=="R":
                        self.head.position+=1
                    elif i[4]=="L":
                        self.head.position-=1
                    else:
                        break
        self.print_line()         
t=Turing(15)
t.add_abc("a")
t.add_abc("b")
t.add_abc("c")
t.add_abc(" ")

t.add_condition("S0")
t.add_condition("S1")
t.add_condition("S2")
t.add_condition("S3")
t.add_condition("S4")
t.add_condition("S5")
t.add_condition("S6")
t.add_condition("S7")
t.add_condition("S8")
t.add_condition("S9")
t.add_condition("S10")
t.add_condition("S11")


t.add_rules([" ", "S0", " ", "S0", "R"])
t.add_rules(["b", "S0", "b", "Q", "Q"])
t.add_rules(["c", "S0", "c", "Q", "Q"])
t.add_rules(["a", "S0", " ", "S1", "R"])
t.add_rules(["b", "S1", " ", "S9", "R"])
t.add_rules(["a", "S9", "a", "Q", "Q"])
t.add_rules(["c", "S1", "c", "Q", "Q"])
t.add_rules(["c", "S9", " ", "S10", "R"])
t.add_rules([" ", "S10", " ", "Q", "Q"])
t.add_rules(["a", "S10", "a", "Q", "Q"])
t.add_rules(["b", "S10", "b", "Q", "Q"])
t.add_rules(["c", "S10", "c", "Q", "Q"])
t.add_rules(["a", "S1", " ", "S2", "R"])
t.add_rules(["a", "S2", "a", "S2", "R"])
t.add_rules(["b", "S2", "a", "S3", "R"])
t.add_rules(["b", "S3", "b", "S3", "R"])
t.add_rules(["a", "S3", "a", "Q", "Q"])
t.add_rules([" ", "S3", "a", "Q", "Q"])
t.add_rules(["c", "S3", "c", "S4", "R"])
t.add_rules(["c", "S4", "c", "S4", "R"])
t.add_rules(["a", "S4", "a", "Q", "Q"])
t.add_rules(["b", "S4", "b", "Q", "Q"])
t.add_rules([" ", "S4", " ", "S5", "L"])
t.add_rules(["c", "S5", " ", "S6", "L"])
t.add_rules(["c", "S6", "c", "S6", "L"])
t.add_rules(["a", "S6", "a", "Q", "Q"])
t.add_rules([" ", "S6", " ", "Q", "Q"])
t.add_rules(["b", "S6", "b", "S7", "L"])
t.add_rules(["b", "S7", "b", "S7", "L"])
t.add_rules(["c", "S7", "c", "Q", "Q"])
t.add_rules(["a", "S7", "a", "S8", "L"])
t.add_rules(["a", "S8", "a", "S8", "L"])
t.add_rules([" ", "S8", " ", "S0", "R"])

t.add_text("aaabbbccc")
