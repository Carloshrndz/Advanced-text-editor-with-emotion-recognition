'''
Input:
- pText(str)
Output:
- relevance (str)
- wordcloud (window)
Restrictions:
- pText must be a string
'''
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def createWordCloud(pText):
    stringsList = pText.lower().replace(",", "").split()
    wordCount = {}

    for word in stringsList:
        if word in wordCount.keys():
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    ordered = dict(sorted(wordCount.items(), key = lambda item: item[1], reverse=True))
    ordered = ordered.keys()
    ordered = list(ordered)

    showingWords = []
    counter = 0
    while (len(ordered)//4 != counter):
        showingWords += [ordered[counter]]
        counter += 1
    mostWords = ""
    for showings in showingWords:
        mostWords += " " + showings
    mostWords = mostWords[1:]

    wordRelevance = mostWords.split()
    relevance = ""
    amount = 0
    relevanceAmount = 1 / wordCount[wordRelevance[0]]
    for ordering in wordRelevance:
        relevance += ordering + ": " +str(wordCount[wordRelevance[amount]]) + "  relevance: " + str(relevanceAmount * wordCount[wordRelevance[amount]]) + " --- "
        amount += 1
    
    cloud = WordCloud().generate(mostWords)
    plt.imshow(cloud)
    plt.axis("off")
    plt.show()
    return relevance[:-5]