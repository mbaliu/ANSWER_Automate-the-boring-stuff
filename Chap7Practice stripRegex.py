#! python3
# stripRegex.py - Realiza a função do str.STRIP(), a qual remove os caracteres
#indicado do início e fim de um string. Sendo que a ordem deles não são importantes.


# A função deverá ter dois argumentos: O STRING, e os CARACTERES
#STRING: o texto que será analisado e operacionalizado
#CHAR: caracteres de referência para a remoção

import re

def splitRegex (char, text):
    global stringrem

    
    if char == '':                              # Regular Expression Object
        iniCHAR = re.compile(r'^\s*')
        finCHAR = re.compile(r'\s*$')
    else:        
        char = '|'.join(list (char))
        iniCHAR = re.compile(str('^('+str(char)+')*'))
        finCHAR = re.compile(str('('+str(char)+')*$'))


    stringrem = iniCHAR.sub('', text)
    stringrem = finCHAR.sub('', stringrem)
    print('-- stringrem defined --')
    return stringrem
    
