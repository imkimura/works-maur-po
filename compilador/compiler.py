import json

class Compiler:
    def __init__(self, fileName="program.cpp"):
        self.fileName = fileName
        self.countline = 1
        self.listmeans = self.initDictWords()
    
    def openFile(self):
        return open(self.fileName, 'r', encoding="utf8")     

    def initDictWords(self):
        with open('listmeans.json') as json_file:
            return json.load(json_file)

    def countlines(self):
        self.countline += 1
    
    def searchMean(self, searchWord):
        if searchWord in self.listmeans:
            
            print("{:^5} | {:^6} | {} ".format(self.countline, searchWord, self.listmeans[searchWord]))
            
            return True   