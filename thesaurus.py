"""
    First, we must develop an API for thesaurus.com, as all the current ones are crap.

    When searching a word (ex: "small"), the synonyms are grouped into three
    categories, differing in presentation by a change in the background color
    of their <span> object.

    The categories are as follows:
        relevant-1
        relevant-2
        relevant-3

    The higher the integer suffix, clearly, the more relevant it is.

    As for the antonyms, they are grouped similarly- however they are of value:
        relevant--1
        relevant--2
        relevant--3

    ...wherein (-3) is the best matching antonym.
"""
# external libraries
import requests
from bs4 import BeautifulSoup

def findRankedSynonyms(inputWord,rank):
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the synonyms
        wordDict = {}
        wordDict['syn3'] = []
        wordDict['syn2'] = []
        wordDict['syn1'] = []
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant-3":
                wordDict['syn3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant-2":
                wordDict['syn2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant-1":
                wordDict['syn1'].append(str(word.text))
                # print(word.text)
            else:
                break

        return wordDict['syn' + str(rank)]

def findRankedAntonyms(inputWord,rank):
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a dictionary to hold all the antonyms
        wordDict = {}
        wordDict['ant3'] = []
        wordDict['ant2'] = []
        wordDict['ant1'] = []
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant--3":
                wordDict['ant3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant--2":
                wordDict['ant2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant--1":
                wordDict['ant1'].append(str(word.text))
                # print(word.text)

        return wordDict['ant' + str(rank)]

def findSynonyms(inputWord):
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a list to hold all the synonyms
        synonyms = []

        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            print(word.text + " " + str(relevanceLevel))
            # if relevanceLevel == ("relevant-3" or "relevant-2" or "relevant-1"):
            #     synonyms.append(str(word.text)) # using str() to remove unicode u''

        return synonyms

def findAntonyms(inputWord):
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        # initialize a list to hold all the antonyms
        wordDict = {}
        wordDict['ant3'] = []
        wordDict['ant2'] = []
        wordDict['ant1'] = []
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant--3":
                wordDict['ant3'].append(str(word.text)) # using str() to remove unicode u''
                # print(word.text)
            elif relevanceLevel == "relevant--2":
                wordDict['ant2'].append(str(word.text))
                # print(word.text)
            elif relevanceLevel == "relevant--1":
                wordDict['ant1'].append(str(word.text))
                # print(word.text)

        return wordDict

synonyms = findSynonyms("big")

for word in synonyms:
    print word

# antonyms = findAntonyms("big")
# print(antonyms)

rankedSyn = findRankedSynonyms("big",1)
print rankedSyn
