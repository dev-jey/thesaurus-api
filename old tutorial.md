If you choose to use the older functions instead of the new Word class, here is the documentation for that code. Eventually, these functions will be phased out... be aware of that.

```python
>>> from thesaurus import *
>>> synonyms = findSynonyms("big") # searches synonyms for "big"
>>> print synonyms
['huge', 'enormous', 'full', 'immense', 'tremendous', 'hefty', 'fat', 'colossal', 'sizable', 'substantial', 'massive', 'gigantic', 'considerable', 'vast', 'ample', 'brimming', 'bulky', 'bull', 'burly', 'capacious', 'chock-full', 'commodious', 'copious', 'crowded', 'extensive', 'hulking', 'humongous', 'husky', 'jumbo', 'mammoth', 'monster', 'packed', 'ponderous', 'prodigious', 'roomy', 'spacious', 'strapping', 'stuffed', 'voluminous', 'whopper', 'whopping', 'awash', 'heavyweight', 'walloping', 'a whale of a', 'heavy-duty', 'mondo', 'oversize', 'super colossal', 'thundering']
```
As you can see, this finds all of the synoyms for the word "big" and places them into a list– however, few of these synonyms are good fits for the word. In order to find the more relevant synonyms, you can use the function "findRankedSynonyms()". Following the lead of thesaurus.com, a synonym of rank 3 is *most* similar to the original word, while a rank of 1 is *least* similar.

As an example:

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

If you are looking for both the synonyms and antonyms of a word in all ranks, you can use findWord(). Ex:

```python
>>> from thesaurus import *
>>> from pprint import pprint
>>> data = findWord("freezing")
>>> pprint(data)
{'ant1': ['boiling', 'heated'],
 'ant2': ['pleasant', 'kind', 'good', 'nice'],
 'ant3': ['tropical', 'friendly', 'responsive', 'amicable', 'hot', 'warm'],
 'syn1': ['gelid',
          'nippy',
          'snappy',
          'shivery',
          'frost-bound',
          'hawkish',
          'one-dog night',
          'two-dog night'],
 'syn2': ['arctic',
          'penetrating',
          'raw',
          'cutting',
          'bitter',
          'chill',
          'chilled',
          'Siberian'],
 'syn3': ['polar',
          'chilly',
          'icy',
          'frigid',
          'biting',
          'glacial',
          'wintry',
          'frosty',
          'numbing']}
```  

Or, if you have a certain word element in mind:

```python
>>> data = findWord("big")['syn1']
>>> print data
['ample', 'brimming', 'bulky', 'bull', 'burly', 'capacious', 'chock-full', 'commodious', 'copious', 'crowded', 'extensive', 'hulking', 'humongous', 'husky', 'jumbo', 'mammoth', 'monster', 'packed', 'ponderous', 'prodigious', 'roomy', 'spacious', 'strapping', 'stuffed', 'voluminous', 'whopper', 'whopping', 'awash', 'heavyweight', 'walloping', 'a whale of a', 'heavy-duty', 'mondo', 'oversize', 'super colossal', 'thundering']
```  

Though, if you are just looking for one element, it would be faster to use `findRankedSynonyms("big",1)`  

If you would prefer a dictionary of synonyms or antonyms organized by rank (rather than a jumbled list), you can use `findWordType("big","syn")`, `findWordType("big","ant")`, or `findWordType("big","all")`. The last of these, wherein type is "all"– is the same as using `findWord()`, though the latter is faster.  

If you wish to get all of the synonyms and antonyms for a word **across its multiple definitions**, there is findWordTotal(). Its output is a large dictionary whose keys are integers ranging from 0 to its length-1. This is so that you can iterate over its values somewhat more easily. To help you differentiate one definition from another, the meaning and partOfSpeech are also included in the sub-dictionaries.
Ex:

```python
>>> from pprint import pprint
>>> data = findWordTotal("dog")
>>> pprint(data)
{'0': {'ant1': [],
       'ant2': [],
       'ant3': [],
       'meaning': u'canine mammal',
       'partOfSpeech': u'noun',
       'syn1': ['bowwow',
                'fido',
                'flea bag',
                'tail-wagger',
                "man's best friend"],
       'syn2': ['cur',
                'stray',
                'tyke',
                'bitch',
                'mutt',
                'hound',
                'mongrel',
                'doggy',
                'pooch'],
       'syn3': ['puppy', 'pup']},
 '1': {'ant1': ['leave alone', 'let go'],
       'ant2': ['run away'],
       'ant3': [],
       'meaning': u'chase after; bother',
       'partOfSpeech': u'verb',
       'syn1': ['bedog'],
       'syn2': ['pursue', 'track', 'trail', 'tail', 'tag', 'trouble'],
       'syn3': ['shadow', 'hound', 'plague', 'haunt']}}
```