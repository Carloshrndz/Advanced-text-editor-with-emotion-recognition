import customtkinter
'''
openFile():
Input:
- path (Str)
Output:
- text (Str); text of the content in the file in path
Constraints:
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
- pText (TextBox)
- pTextToFind (Str)
- pTextReplace (Str)
- pAmount (Int) | (Bool)
Output:
- output (Str); The resulting text after performing the replacement(s)
Constraints:
- pAmount must be a non-negative integer or a boolean.
'''    
def findReplace(pText, pTextToFind, pTextReplace, pAmount = False):
    
    try:
        pAmount = int(pAmount)
    except:
        pAmount == False
    if pAmount == False:
        output = pText.get(0.0, 'end').replace(pTextToFind, pTextReplace)
        pText.delete(0.0, 'end')
        return pText.insert(0.0, output)
    else:
        output = pText.get(0.0, 'end').replace(pTextToFind, pTextReplace, pAmount)
        pText.delete(0.0, 'end')
        return pText.insert(0.0, output)



'''
wordCounter():
Input:
- pText
Output:
- len(words)(Int); Amount of Words in pText
- len(diferentsWords)(Int); Amount of diferents words in pText
Constraints:
- pText must be a valid string
'''
def wordCounter(pText):
    symbols = [',', '.', ';', '?', '!']
    for symbol in symbols:
        pText = pText.replace(symbol, '')
    words = pText.lower().split()
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
Constraints:
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