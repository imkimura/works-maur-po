from compiler import Compiler

if __name__ == '__main__':
    
    c = Compiler()
    
    readCode = c.openFile()

    readCodeLines = readCode.readlines()
       
    print("{:^5} | {:^6} | {:^22} ".format("Line","Token","Mean"))
    
    for line in readCodeLines:
        
        if line[0] == '#':
            print("{:^5} | {:^6} | Ignora a linha ".format(c.countline, line[0]))
            c.countlines()
            pass
        else:            
            wordsSplited = line.split()

            for word in wordsSplited:
                if c.searchMean(word):
                    continue
                else:   
                    auxword = ''                    
                    
                    for letter in word:
                        
                        if letter == ' ':
                            continue
                        
                        if c.searchMean(letter):
                            auxword = ''
                            continue

                        auxword += letter
                        if c.searchMean(auxword):
                            auxword = ''
                
            c.countlines()      