from key import Key

class HashingTable:
    def insertKey(end, key):
        if end[key%100] is not None:
            p = end[key%100]                
            while(p.getProx()):
                p = p.getProx()                
            p.prox = Key(key)                   
        else:
            end[key%100] = Key(key)  
            
    def searchKey(end, search):
        for i, e in zip(range(0, len(end)), end):                    
            if i == search%100:
                if e is None:
                    print("\n\nChave não existente na tabela")
                else:
                    found = False
                    p = e
                    while(p.getProx() is not None):
                        if p.getKey() == search:
                            print("\n\nChave "+ str(search) + " encontrada no endereço " + str(i))
                            found = True
                            break
                        else:
                            p = p.getProx()
                    if found:
                        pass
                    else:
                        if p.getKey() == search:
                            print("\n\nChave "+ str(search) + " encontrada no endereço " + str(i))
                        else:
                            print("\n\nChave não existente na tabela")
    def printList(end):
        for i, e in zip(range(0, len(end)), end):                    
            if e is not None:                                        
                p = e
                txt = '\nEndereço: ' + str(i) +'  ||  Chaves: ' + str(e.getKey())
                while(p.getProx() is not None):
                    p = p.getProx()
                    txt += ' -> ' + str(p.getKey())
                print(txt)
    
    loop = True
    end = [None] * 100
    
    while(loop):
        op = input("\n\nSeja bem vindo(a) ao sistema de tabela hashing! \nEscolha uma opção para continuar: \n\n [1] - Inserir Chaves (Apenas Inteiros)\n [2] - Buscar Chave na Tabela\n [3] - Imprimir Tabela\n [0] - Sair\n\nInsira sua escolha: ")
        if op == '1':
            key = int(input("Insira uma chave:: "))
            insertKey(end, key)
                                      
        elif op == '2':
            search = int(input("Insira uma chave que deseja procurar:: "))
            searchKey(end, search)

        elif op == '3':
            printList(end)
        
        elif op == '0':
            loop = False
        
        else:
            print("\n\nNão temos essa opção.")
            pass

if __name__ == '__main__':       
    HashingTable()
