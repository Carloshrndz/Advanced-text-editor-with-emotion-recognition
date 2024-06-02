'''
openFile():
Input:
- path (Str)
Output:
- text (Str); text of the content in the file in path
Restrictions:
- path must be a valid path
'''
def openFile(pPath):
    try:
        file = open(pPath, 'r')
        content = file.read()
        file.close()
        return content, True
    except Exception as e:
        return e, False
    
    
'''
findReplace():
Input:
- pText (Str)
- pTextToFind (Str)
- pTextReplace (Str)
- pAmount (Int) | (Bool)
Output:
- output (Str); The resulting text after performing the replacement(s)
Restrictions:
- pAmount must be a non-negative integer or a boolean.
'''    
def findReplace(pText, pTextToFind, pTextReplace, pAmount = True):
    if pAmount == True:
        output = pText.replace(pTextToFind, pTextReplace)
    else:
        output = pText.replace(pTextToFind, pTextReplace, pAmount)
    return output


'''
wordCounter():
Input:
- pText
Output:
- len(words)(Int); Amount of Words in pText
- len(diferentsWords)(Int); Amount of diferents words in pText
Restrictions:
- pText must be a valid string
'''
def wordCounter(pText):
    words = pText.split()
    diferentWords = []
    for word in words:
        if word not in diferentWords:
            diferentWords += [word]
    return len(words), len(diferentWords)


'''
saveText():
Input:
- pText (Str)
- pPath (Str)
Output:
- (Boolean) | (Str); Returns True or an string of an exception
Restrictions:
- path must be a valid path
'''
def saveText(pText, pPath):
    try:
        file = open(pPath, 'w')
        file.write(pText)
        file.close()
        return True
    except Exception as e:
        return e