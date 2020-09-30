import json

class Compiler:
    def __init__(self, fileName="program.cpp"):
        self.fileName = fileName
        self.countline = 1
        self.listmeans = self.initDictWords()
        self.syntaxlist = self.initDictSyntax()
        self.grammarlist = self.initDictGrammar()
        self.tokenstack = []
    def openFile(self):
        return open(self.fileName, 'r', encoding="utf8")     

    def initDictWords(self):
        with open('listmeans.json') as json_file:
            return json.load(json_file)
            
    def initDictSyntax(self):
        with open('syntaxtable.json') as json_file:
            return json.load(json_file)
    
    def initDictGrammar(self):
        with open('grammarrules.json') as json_file:
            return json.load(json_file)

    def countlines(self):
        self.countline += 1
    
    def searchMean(self, searchWord):
        if searchWord in self.listmeans:
            
            print("{:^5} | {:^6} | {} ".format(self.countline, searchWord, self.listmeans[searchWord]))
            self.tokenstack.append(searchWord) #unfinished stack method
            return True
    
    def First(self, symbol):
        if symbol in self.grammarlist:
            for rule in self.grammarlist[symbol]:
                firstsymbol = list(rule)[0]

                if firstsymbol in self.grammarlist:
                    return First(firstsymbol)
                else:
                    #unfinished again    



