
class Melc:
    def __init__(self):
        self.inIf = False
        self.inElse = False
        self.inWhile = False
        self.inMain = True

    def changeIfState(self):
        if self.inIf == True:
            print("L3 NADA")
            self.inIf = False

    def changeElseState(self):
        if self.inElse == True:
            print("L4 NADA")
            self.inElse = False

    def changeWhileState(self):
        if self.inWhile == True:
            print("DSVS L1")
            print("L2 NADA")
            self.inWhile = False

    def variable(self, line):
        wordSplited = line.split()
        if wordSplited[2].isnumeric():
            #atribuiçao
            print("CRCT {}".format(wordSplited[2]))
            if wordSplited[0] == 'A':
                print("ARMZ 0")
            else:
                print("ARMZ 1")
        else:
            #soma
            if wordSplited[4].isnumeric():
                print("CRVL 0")
                print("CRCT 1")
                print("SOMA")
                print("ARMZ 0")
                self.changeElseState()
                
            else:
                print("CRVL 1")
                print("CRVL 2")
                print("SOMA")
                print("ARMZ 1")
                self.changeElseState()
                

    def reservedWord(self, line):
        wordSplited = line.split()
        if wordSplited[0] == 'main':
            self.inIf = True
            print("INPP")
        elif wordSplited[0] == 'int':
            counter = len(wordSplited) - 2
            print("AMEM {}".format(counter))
        elif wordSplited[0] == 'printf':
            if wordSplited[3] == 'S':
                print("CRVL 1")
                print("IMPR")
        elif wordSplited[0] == 'scanf':
            print("LEIT")
            word = wordSplited[3].replace('&', '')
            if word == 'NUM':
                print("ARMZ 2")
        elif wordSplited[0] == 'if':
            self.inIf = True
            if wordSplited[2] == 'NUM':
                print("CRVL 2")
            print("CRCT {}".format(wordSplited[4]))
            if wordSplited[3] == '>':
                print("CMMA")
            print("DSVF L3")
        elif wordSplited[0] == 'else':
            self.inElse = True
            print("DSVS L4")
            self.changeIfState()
        elif wordSplited[0] == 'while':
            self.inWhile = True
            print("L1 NADA")
            if wordSplited[2] == 'A':
                print("CRVL 0")
            print("CRCT {}".format(wordSplited[4]))
            if wordSplited[3] == '<=':
                print("CMEG")
            print("DSVF L2")

    def specialSymbol(self, line):
        wordSplited = line.split()
        if wordSplited[0] == '}':
            if self.inWhile == True:
                self.changeWhileState()
            elif self.inMain == True:
                print("DMEM 3")
                print("PARA")

    def multiSymbol(self, line):
        pass
