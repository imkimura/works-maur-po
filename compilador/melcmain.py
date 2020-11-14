code = open('melcProgram.cpp', 'r', encoding="utf8")
compiler = Compiler()
melc = Melc()

for line in code.readlines():
    if line[0] == '#':
            pass
        else:            
            wordsSplited = line.split()
            verifyString = False
            for word in wordsSplited:
                if verifyString == False and mean = compiler.searchWord(word):
                    melc.checkToken(word, mean)
                    continue
                else:

                    for letter in word:
                        
                        if verifyString:
                            if letter == chr(34):
                                verifyString = False
                        else:
                            if letter == chr(34):
                                verifyString = True
                                continue
                            
                            if letter == ' ':
                                continue
                            
                            if mean = compiler.searchWord(letter):
                                melc.checkToken(letter, mean)
                                auxword = ''
                                continue

                            auxword += letter

                            if compiler.searchWord(auxword):
                                melc.checkToken(auxword, mean)
                                auxword = ''

                    if auxword:
                        melc.checkToken(auxword, 'Variavel')

                    auxword = ''

            compiler.countlines()
