class Key:
    def __init__(self, value, prox=None):
        self.value = value
        if(prox):
            self.prox = prox

    def getKey(self):
        return self.value
    
    def setKey(self, value):
        self.value = value

if __name__ == '__main__':    
    loop = True
    end = [None] * 100
    while(loop):
        op = int(input("Insira uma opção:: "))
        if op == 1:
            print("Teste")
        elif op == 2:
            print("Teste")
        elif op == 3:
            for e in end:    
                print("Teste")
        else:
            print("Teste")
            loop = False
