#! python3
# regexSearcher - searches all matches in a directory.

'''
Abre todos os arquivos .txt de um diretório
Localiza todos os textos que batem com o regex
Imprimi todas os casos localizados.
'''

#TODO: Identifica a pasta e o RegExp

#TODO: Lê todos os arquivos .txt de uma pasta

#TODO: imprimi todos localizados

import os, re

# Identifica a pasta e o RegExp, e verifica se é um diretório
while True:
    sdir = input ('Inserir o diretório: ')
    if os.path.isdir(sdir):
        break
        
regexObj = re.compile(input ('Inserir o Regular Expression: '))

# Lista os arquivos .txt de uma pasta
files = os.listdir(sdir)
s_files = []
for i in files:
    if i.endswith('.txt'):              # condicional
        s_files.append(i)               # adiciona à lista de arquivos

# Abre cada um dos arquivos para procurar
for i in s_files:
    fullname = os.path.join(sdir, i)
    file = open(fullname,'r')
    rfile = file.read()
    # print(fullname) # to check the names
    
    matchObj = regexObj.findall(rfile, re.IGNORECASE)
    # imprimi cada lista e o nome do arquivo
    print(str(matchObj) + ' in: ' + str(i))

    
    file.close()
