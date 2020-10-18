import json

def initDictGrammar():
    with open('grammarrules.json') as json_file:
        return json.load(json_file)

def initDictSyntax():
    with open('syntaxtable.json') as json_file:
        return json.load(json_file)

syntaxlist = initDictSyntax()
terminals = initDictGrammar()['terminals']
nonterminals = initDictGrammar()['nonterminals']
stack = ["$", "E"]

buffer = input("Cadeia: ")
buffer += ' $'
buffer = buffer.split(" ")

print('Stack: ',stack)

def firstInBuffer():
    return buffer[0]

def firstInStack(): 
    return stack[len(stack)-1]

while len(stack) != 1: #while stack is not empty

    if firstInStack() in terminals:

        print('Buffer: ', buffer)
        print('Action: -----')
        print('')

        if firstInBuffer() == firstInStack():
            buffer.pop(0)
            stack.pop()
        else:
            #Error, token in buffer is not the same as in stack
            print("ERROR")
            break
        print('Stack: ',stack)

    elif firstInStack() in nonterminals: 
        action = syntaxlist[firstInStack()][firstInBuffer()]
        
        print('Buffer: ', buffer)
        print('Action: ', firstInStack(), '->', action)
        print('')

        if action == 'ERROR':
            print('ERROR')
            break
        stack.pop()

        for symbol in reversed(action):
            if symbol != 'LAMBDA': #char 'λ' was having problems, replaced with 'LAMBDA'
                stack.append(symbol)

        print('Stack: ',stack)
        
    else:
        #Error, token wasnt recognized 
        print("ERROR")
        break

if buffer[0] == '$':
    print('Buffer: ', buffer)
    print('Action: SUCCESS')