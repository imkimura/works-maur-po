class Key:
    def __init__(self, value, prox=None):
        self.value = value        
        self.prox = None

    def getKey(self):
        return self.value
    
    def setKey(self, value):
        self.value = value

    def getProx(self):
        return self.prox
    
    def __str__(self):
        return "({}, {})".format(self.value, self.prox)

if __name__ == '__main__':    
    loop = True
    end = [None] * 100
    while(loop):
        op = int(input("Insira uma opção:: "))
        if op == 1:
            val = int(input("Insira uma chave:: "))
            if end[val%100] is not None:
                p = end[val%100]
                print(p)
                while(p.getProx()):
                    p = p.getProx()
                    print(p)
                p = Key(val)
                print(p)
            else:
                end[val%100] = Key(val)
        elif op == 2:
            print("Teste")
        elif op == 3:
            for e in end:    
                if e is not None:
                    v = str(e.getKey())
                    p = e
                    print(str(e.getKey()))
                    while(p.getProx() is not None):
                        p = p.getProx()
                        print(str(e.getKey()))
                    print(str(e.getKey()))
        else:
            print("Teste")
            loop = False
