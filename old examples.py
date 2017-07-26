import requests
from bs4 import BeautifulSoup
from thesaurus import *
from pprint import pprint

# ===========================   RANKED SYNONYMS   ==============================
"""
    All synonyms of rank three.
"""
rankedSynonyms = findRankedSynonyms("big",3)
print len(rankedSynonyms)
for item in rankedSynonyms:
    print item

# ===========================   RANKED ANTONYMS   ==============================
"""
    All antonyms of rank three.
"""
rankedAntonyms = findRankedAntonyms("big",3)
print len(rankedAntonyms)
for item in rankedAntonyms:
    print item

# ===============================   SYNONYMS   =================================
"""
    All synonyms.
"""
synonyms = findSynonyms("big")
print len(synonyms)
for item in synonyms:
    print item

# ===============================   ANTONYMS   =================================
"""
    All antonyms.
"""
antonyms = findAntonyms("big")
print len(antonyms)
for item in antonyms:
    print item

# ================   COMBINED DICTIONARY OF ALL DEFINITIONS   ==================
"""
    All synonyms and antonyms across all definitions.
"""
data = findWordTotal('object')

wordDict = {}
for y in xrange(-3,3+1):
    if y < 0:
        wordDict['ant'+str(abs(y))] = []
    elif y > 0:
        wordDict['syn'+str(y)] = []

for x in xrange(0,len(data)):
    # x corresponds to the current number of the definition.
    for y in xrange(-3,3+1):
        if y < 0:
            wordDict['ant'+str(abs(y))].extend(data[str(x)]['ant'+str(abs(y))])
            wordDict['ant'+str(abs(y))] = list(set(wordDict['ant'+str(abs(y))]))
        elif y > 0:
            wordDict['syn'+str(y)].extend(data[str(x)]['syn'+str(y)])
            wordDict['syn'+str(y)] = list(set(wordDict['syn'+str(y)]))

pprint(wordDict)
