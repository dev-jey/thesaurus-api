import requests
from bs4 import BeautifulSoup

#set up the soup of beauty
# url = "http://www.thesaurus.com/browse/big"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "html.parser")
#
# tag = soup.select("div#synonyms-0 section.container-info.antonyms div.list-holder ul.list li a span.text")
# # tag = soup.find_all("div", {"id" : "synonyms-0"})
# for element in tag:
#     print element.text

"""
<a href="http://www.thesaurus.com/browse/baby" class="common-word" data-id="59" data-category="{&quot;name&quot;: &quot;relevant--1&quot;, &quot;color&quot;: &quot;#f1f2f2&quot;}" data-complexity="1" data-length="1" style="background-color: rgb(241, 242, 242); font-weight: 400; color: rgb(51, 51, 51);"><span class="text">baby</span></a>

<a href="http://www.thesaurus.com/browse/baby" class="common-word" data-id="35" data-category="{&quot;name&quot;: &quot;relevant--1&quot;, &quot;color&quot;: &quot;#f1f2f2&quot;}" data-complexity="1" data-length="1"><span class="text">baby</span></a>
"""
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


# ===========================   RANKED ANTONYMS   ==============================
rankedAntonyms = findRankedAntonyms("big",1)
print len(rankedAntonyms)
for item in rankedAntonyms:
    print item
