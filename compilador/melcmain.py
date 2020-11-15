from compiler import Compiler
from melc import Melc

code = open('melcProgram.cpp', 'r', encoding="utf8")
compiler = Compiler()
melc = Melc()

for line in code.readlines():
    if line[0] == '#':
        pass
    else:           
        for word in line.split():
            mean = compiler.searchWord(word)
            if mean != False:
                if mean == "Palavras Reservadas":
                    melc.reservedWord(line)
                elif mean == "Simbolo especial":
                    melc.specialSymbol(line)
                elif mean == "Simbolo Composto":
                    melc.multiSymbol(line)
                break
            else:
                melc.variable(line)
                break

