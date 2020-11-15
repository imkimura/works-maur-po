
class Melc:
    def checkToken(self, token, mean):
        if mean == 'Variavel':
            print("do shit")
        elif mean == 'Simbolo especial':
            print("do shit")
        elif mean == 'Palavras Reservadas':
            print("do shit")
            if token == 'main':
                print("INPP")
            elif token == 'int':
                print("AMEM 3")

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
            else:
                print("CRVL 1")
                print("CRVL 2")
                print("SOMA")
                print("ARMZ 1")

    def reservedWord(self, line):
        pass

    def specialSymbol(self, line):
        pass

    def multiSymbol(self, line):
        pass