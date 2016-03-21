"""
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
        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

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
            # if relevanceLevel == "relevant-1":
            #     print("***** - " + word.text + " " + str(relevanceLevel))
            # else:
            #     print(word.text + " " + str(relevanceLevel))
            if (relevanceLevel == "relevant-3"):
                # print(word.text)
                synonyms.append(str(word.text)) # using str() to remove unicode u''
            elif (relevanceLevel == "relevant-2"):
                # print(word.text)
                synonyms.append(str(word.text))
            elif (relevanceLevel == "relevant-1"):
                # print(word.text)
                synonyms.append(str(word.text))
            else:
                """
                Thanks to thesaurus.com's developers, there are sometimes up to
                11 copies of given words. (Ex: search for /browse/baby on the
                page for the word "big"). In order to combat this, I am stopping
                the loop before it reaches the antonyms, as it repeats afterwards.

                I may eventually change this to only select elements with background
                colors or font weights, as the hidden words do not have any styles.
                """
                break

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
        antonyms = []

        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            # print(relevanceLevel + word.text)
            if relevanceLevel == "relevant--3" or "relevant--2" or "relevant--1":
                antonyms.append(str(word.text)) # using str() to remove unicode u''

        return antonyms\

def findWord(inputWord):
    """
        Combine both synonyms and antonyms into a large dictionary of mult.
        itemtypes.

        Now, I was considering having this just call the findRankedAntonyms and
        findRankedSynonyms and building the dictionary this way... However that
        is much slower. Here are the times as comparison:

        # individual function calls
                2.39 real         0.93 user         0.06 sys
                2.24 real         0.94 user         0.05 sys
                1.86 real         0.98 user         0.06 sys
                average : 2.1633333333

        # normal function
                0.55 real         0.25 user         0.04 sys
                0.37 real         0.24 user         0.03 sys
                0.37 real         0.24 user         0.03 sys
                average: 0.4033333333

        as you can see, it is much faster to use the current html document than
        calling a function that has to reload it each time.
    """
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

        # synonyms
        wordDict['syn3'] = []
        wordDict['syn2'] = []
        wordDict['syn1'] = []

        #antonyms
        wordDict['ant3'] = []
        wordDict['ant2'] = []
        wordDict['ant1'] = []
        wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

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

        wordTags = soup.select("div#synonyms-0 div#filters-0 div.relevancy-block div.relevancy-list ul li a span.text")

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

        return wordDict

def findWordType(inputWord,type):
    """
    Same as findAntonyms or findSynonyms, however it returns them in an
    organized dictionary.
    """
    type = cleanInput(type)

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
        if type == 'syn':
            # synonyms
            wordDict['syn3'] = []
            wordDict['syn2'] = []
            wordDict['syn1'] = []

            wordTags = soup.select("div#synonyms-0 div#filters-0 div.relevancy-block div.relevancy-list ul li a span.text")

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
        elif type == 'ant':
            #antonyms
            wordDict['ant3'] = []
            wordDict['ant2'] = []
            wordDict['ant1'] = []

            wordTags = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")

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
        elif type == "all":
            wordDict = findWord(inputWord)
        else:
            print("ERROR: Not 'ant', 'syn', or 'all'.")
            return {}

        return wordDict

def cleanInput(inputString):
    inputString = inputString.lower()

    return inputString
