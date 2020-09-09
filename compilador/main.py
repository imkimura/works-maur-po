from compiler import Compiler

if __name__ == '__main__':
    auxword = '' 
    compiler = Compiler()
    
    readCode = compiler.openFile()

    readCodeLines = readCode.readlines()
       
    print("{:^5} | {:^6} | {:^22} ".format("Line","Token","Mean"))
    
    for line in readCodeLines:
        
        if line[0] == '#':
            print("{:^5} | {:^6} | Ignora a linha ".format(compiler.countline, line[0]))
            compiler.countlines()
            pass
        else:            
            wordsSplited = line.split()

            for word in wordsSplited:
                if compiler.searchMean(word):
                    continue
                else:
                    
                    for letter in word:
                        
                        if letter == ' ':
                            continue
                        
                        if compiler.searchMean(letter):
                            auxword = ''
                            continue

                        auxword += letter

                        if compiler.searchMean(auxword):
                            auxword = ''

                    if auxword:
                        print("{:^5} | {:^6} | {} ".format(compiler.countline, auxword, 'Variável'))
                    auxword = ''

            compiler.countlines()