#! python3
# dateFormater.py - converts differents dates formats in a single format

''' -------------
1. Cola e copia do clipboard
    2. identifica datas
3. Identifica o formato (NOT)
4. Converte para o padrão definido
-----------------


'''

import pyperclip, re

def strFormater (numStr):
    numStr = str(numStr)
    lenFinal = 2
    add = lenFinal - len(numStr)
    numStr = '0'*add + numStr
    return numStr


def dateFormater ():
    dates = pyperclip.paste()

    # Para o modelo de DataScience
    dateObj = re.compile(r'''(
        (\d{1,2})       # dias      1
        (-|/|.|_)       # divisor   2
        (\d{1,2})       # mês       3
        (-|/|.|_)       # divisor   4
        (\d{4})         # ano       5
        )''', re.VERBOSE)
    # Atenção para a definição da quantidade: {inicío , fim}

    dateElem = dateObj.findall(dates)
    modelo = input('Modelo de data (amd, dma ou mda): ')
    join = str( input ('Tipo de conector: '))


    for date in dateElem:
        ano = [date[5]]
        mes = [strFormater(date[3])]
        dia = [strFormater(date[1])]

        
        if modelo == 'amd':
            nDate = join.join( ano + mes + dia )
        elif modelo == 'mda':
            nDate = join.join( mes + dia + ano )
        elif modelo == 'dma':
            nDate = join.join( dia + mes + ano )
        else:
            nDate = join.join( ano + mes + dia )
            
        print(nDate)
