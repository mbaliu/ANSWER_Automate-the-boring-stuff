#! python3
# httpURL: localizar urls com http ou https
'''
Pegar o texto no clipboard
Achar todos os URL
Colar no clipboard
'''

import pyperclip, re

def httpFind():
        clipboard = pyperclip.paste()

        URLsRegex = re.compile (r'''(
            (http://|https://)              # Identificador URL
            (\S|[._/=#?&-])+
            )''', re.VERBOSE)



        URLs = URLsRegex.findall(clipboard)

        matches = [ ]                       #Criação do campo dos resultado



        for site in URLs:
                matches.append(site[0])            #Adição dos itens ao resultado
                                            #Criação de uma lista com resultados,
                                            #ao invés de um tuple

        print('\n'.join(matches))           #Transformação de lista em um STRING único
        pyperclip.copy('\n'.join(matches))
