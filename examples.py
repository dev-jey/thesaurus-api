import requests
from bs4 import BeautifulSoup
from thesaurus import *

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
