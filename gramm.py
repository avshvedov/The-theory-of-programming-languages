import random

class gramm:
    __rules=[]

    def add_rule(self, S):
        self.__rules.append(S)

    def add_rules_list(self, rules_list):
        for rule in rules_list:
            self.__rules.append(rule)
    def look(self):
        return self.__rules

    def deduct(self, L, n):
        while (n!=0):
            r=random.randint(0, len(self.__rules)-1)
            st=self.__rules[r]
            if L.find(st[0])!=-1:
                L=L.replace(st[0],st[1])
            n-=1
        return L

a=gramm()
#a.add_rule(["S","(S)"])
#a.add_rule(["S","SS"])
#a.add_rule(["S",""])
a.add_rules_list([["D", "B."],
           ["N", "+"],["N", "-"],
           ["B", "N0"],["B", "N1"],["B", "0"],["B", "1"],["B", "B0"],["B", "B1"],
           ["P", "D0"],["P", "D1"],["P", "P0"],["P", "P1"],["P", "0"],["P", "1"],["P", "N0"],["P", "N1"]])
