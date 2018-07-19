#! python3
# lucky.py - Opens several Google search results.
# No cmd, py Proj_Chap11_lucky.py __item a ser procurado__

import requests, sys, webbrowser, bs4


# Read the cmd line arg from sys.argv
# Fetch the search result page with the requests module

print('Googling...')    #display text while downloading the google page
cmdRead = sys.argv[1:]
res =  requests.get('http://google.com/search?q=' + ' '.join(cmdRead))
res.raise_for_status()


# Retrive top search results links.
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

# TD Open a browser tab for each result.
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
