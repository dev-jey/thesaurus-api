import requests
from bs4 import BeautifulSoup
from thesaurus import *

# wordDict = findWord("big")
wordDict = findWordType("big",'all')

#synonyms
print("\nsyn3:")
print wordDict['syn3']
print("\nsyn2:")
print wordDict['syn2']
print("\nsyn1:")
print wordDict['syn1']

#antonyms
print("\nant3:")
print wordDict['ant3']
print("\nant2:")
print wordDict['ant2']
print("\nant1:")
print wordDict['ant1']
