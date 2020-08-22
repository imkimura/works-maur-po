class Compiler:
    
    
    
    listmeans = dict()
    
    listmeans = {
                    'auto': 'Palavras Reservadas', 
                    'break': 'Palavras Reservadas', 
                    'case': 'Palavras Reservadas', 
                    'char': 'Palavras Reservadas',
                    'const': 'Palavras Reservadas',
                    'continue': 'Palavras Reservadas',
                    'default': 'Palavras Reservadas',
                    'do': 'Palavras Reservadas',
                    'double': 'Palavras Reservadas',
                    'else': 'Palavras Reservadas',
                    'enum': 'Palavras Reservadas',
                    'extern': 'Palavras Reservadas',
                    'float': 'Palavras Reservadas',
                    'for': 'Palavras Reservadas',
                    'goto': 'Palavras Reservadas',
                    'if': 'Palavras Reservadas',
                    'int': 'Palavras Reservadas',
                    'long': 'Palavras Reservadas',
                    'register': 'Palavras Reservadas',
                    'return': 'Palavras Reservadas',
                    'short': 'Palavras Reservadas',
                    'signed': 'Palavras Reservadas',
                    'sizeof': 'Palavras Reservadas',
                    'static': 'Palavras Reservadas',
                    'struct': 'Palavras Reservadas',
                    'switch': 'Palavras Reservadas',
                    'typedef': 'Palavras Reservadas',
                    'union': 'Palavras Reservadas',
                    'unsigned': 'Palavras Reservadas',
                    'void': 'Palavras Reservadas',
                    'volatile': 'Palavras Reservadas',
                    'while': 'Palavras Reservadas',
                    '.': 'Símbolo Especial', 
                    ';': 'Símbolo Especial', 
                    ',': 'Símbolo Especial', 
                    '(': 'Símbolo Especial', 
                    ')': 'Símbolo Especial', 
                    ':': 'Símbolo Especial',
                    '+': 'Símbolo Especial', 
                    '<': 'Símbolo Especial', 
                    '>': 'Símbolo Especial', 
                    '+': 'Símbolo Especial', 
                    '-': 'Símbolo Especial', 
                    '*': 'Símbolo Especial', 
                    '%': 'Símbolo Especial',
                    '++': 'Símbolo Composto', 
                    '--': 'Símbolo Composto', 
                    '>=': 'Símbolo Composto',
                    '<=': 'Símbolo Composto', 
                    '+=': 'Símbolo Composto', 
                    '-=': 'Símbolo Composto', 
                    '*=': 'Símbolo Composto', 
                    '/=': 'Símbolo Composto', 
                    '%=': 'Símbolo Composto'
                }                 

    if 'auto' in listmeans:
        print(listmeans.get('auto'))

    for a in program:
        print(a)    

if __name__ == '__main__':
    Compiler()

