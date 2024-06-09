import spacy
nlp = spacy.load('en_core_web_sm')


'''
inputs:
- pText(str)
Outputs:
- matrix(list)
Restrictions:
- pText must be a string
'''

def getWords(pNlp):
    output = []
    for token in pNlp:
        if not token.is_stop and not token.is_punct and not token.is_space:
            output += [token.text.lower()]
    return output



def createIndexDict(pList):
    output = {}
    for index, word in enumerate(pList):
        output[word] = index
    return output
        
        
        
def createMatrix(pText):
    doc = nlp(pText)
    words = sorted(set(getWords(doc)))
    matrix = []
    for row in range(len(words)):
        matrix.append([0])
        for _ in range(len(words) - 1):
            matrix[row].append(0)
    
    
    wordIndexSearch = createIndexDict(words)
    
    for sentence in doc.sents:
        sentWords = getWords(sentence)
        for indexInSentence1 in range(len(sentWords)):
            for indexInSentence2 in range(indexInSentence1 + 1, len(sentWords)):
                indexInSearch1 = wordIndexSearch[sentWords[indexInSentence1]]
                indexInSearch2 = wordIndexSearch[sentWords[indexInSentence2]]
                matrix[indexInSearch1][indexInSearch2] += 1
                matrix[indexInSearch2][indexInSearch1] += 1
    return matrix, words

def createCoocurrence(pText):
    matrix, words = createMatrix(pText)
    
    output = [[''] + words]
    for i, word in enumerate(words):
        output.append([word] + matrix[i])
    return output
