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
         