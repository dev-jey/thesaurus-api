# Thesaurus-API
Greetings, and welcome to the unofficial api for thesaurus.com. A few of these functions were originally written for an [acronym creator](https://github.com/Manwholikespie/backronym), however I figured other people might want to pull data from thesaurus.com.

## Introduction
With the thesaurus-api, you are able to grab synonyms and antonyms from thesaurus.com. Thanks to the way the website highlights synonym/antonym entries in different colors according to their relevance, I have also included functions to grab certain ranks of syn/ant entries according to the level of relevance you require.

## License
Everything in here is licensed under the MIT license. Do with it what you want– make some money. Just don't get me involved.

## Getting Started
First, download the program.  
`git clone https://github.com/Manwholikespie/thesaurus-api`  

Next, navigate to its directory and launch python. 
```fish
Prog λ cd thesaurus-api/
thesaurus-api:master* λ python
```

In python, the syntax is fairly simple.
```python
>>> from thesaurus import *
>>> synonyms = findSynonyms("big") # searches synonyms for "big"
>>> print synonyms
['huge', 'enormous', 'full', 'immense', 'tremendous', 'hefty', 'fat', 'colossal', 'sizable', 'substantial', 'massive', 'gigantic', 'considerable', 'vast', 'ample', 'brimming', 'bulky', 'bull', 'burly', 'capacious', 'chock-full', 'commodious', 'copious', 'crowded', 'extensive', 'hulking', 'humongous', 'husky', 'jumbo', 'mammoth', 'monster', 'packed', 'ponderous', 'prodigious', 'roomy', 'spacious', 'strapping', 'stuffed', 'voluminous', 'whopper', 'whopping', 'awash', 'heavyweight', 'walloping', 'a whale of a', 'heavy-duty', 'mondo', 'oversize', 'super colossal', 'thundering']
```
As you can see, this finds all of the synoyms for the word "big" and places them into a list– however, few of these synonyms are good fits for the word. In order to find the more relevant synonyms, you can use the function "findRankedSynonyms()". As an example:
```python
>>> rankedSynonyms = findRankedSynonyms("big",3) # finds synonyms of rank 3.
>>> print rankedSynonyms
['huge', 'enormous', 'full', 'immense', 'tremendous', 'hefty', 'fat', 'colossal', 'sizable', 'substantial', 'massive', 'gigantic', 'considerable', 'vast']
```
The antonyms follow the same syntax...
```python
>>> antonyms = findAntonyms("big")
>>> print antonyms
['miniature', 'teeny', 'tiny', 'insignificant', 'unimportant', 'impoverished', 'inconsiderable', 'blah', 'adolescent', 'baby', 'babyish', 'infantile', 'juvenile', 'selfish', 'ungenerous', 'little', 'minute', 'small', 'slight', 'thin', 'poor', 'bland', 'dull', 'infant', 'ungiving', 'humble', 'shy', 'unconfident', 'itsy']
>>> rankedAntonyms = findRankedAntonyms("big",3)
>>> print rankedAntonyms
['miniature', 'teeny', 'tiny', 'insignificant', 'unimportant', 'impoverished', 'inconsiderable', 'little', 'minute', 'small', 'slight', 'thin', 'poor']
```

## Coming Soon
I will soon make a findWord(inputWord) function that will return both synonyms and antonyms of individual ranks into a dictionary.

Also, there will be another function that allows you to search for the synonyms/antonyms of a different definition of the word you are searching for (right now those are hidden in different tabs, but I should be able to fix that by changing the beautifulsoup selector to div#synonyms-[1,2,3, etc.].

## Special Thanks
To [James](https://github.com/jaykm/) for the idea to just use rstrip() instead of something much more complicated to single-out an entry's relevanceLevel.
