'''
inputs:
- pText(str)
Outputs:
- matrix(list)
Restrictions:
- pText must be a string
'''

def co_occurrence(pText):
    if not isinstance(pText, str):
        raise ValueError("The input pText must be a string")

    stringsList = pText.lower().replace(",", "").replace(".", "").replace("an", "").replace("the", "").replace("a", "").replace("and", "").replace("but", "")\
        .replace("or", "").replace("nor", "").replace("for", "").replace("so", "").replace("yet", "").replace("although", "").replace("because", "")\
        .replace("since", "").replace("unless", "").replace("while", "").replace("if", "").replace("when", "").replace("as", "").split()
    
    wordCount = {}
    for word in stringsList:
        wordCount[word] = wordCount.get(word, 0) + 1

    words = list(wordCount.keys())

    matrix_size = len(words)
    matrix = [[0] * (matrix_size + 1) for _ in range(matrix_size + 1)]
    

    for i in range(1, matrix_size + 1):
        matrix[0][i] = words[i - 1]
        matrix[i][0] = words[i - 1]
    

    for i in range(1, matrix_size + 1):
        for j in range(1, matrix_size + 1):
            if i == j:
                matrix[i][j] = wordCount[words[i - 1]]
            else:
                count = 0
                for k in range(len(stringsList) - 1):
                    if stringsList[k] == words[i - 1] and stringsList[k + 1] == words[j - 1]:
                        count += 1
                    elif stringsList[k] == words[j - 1] and stringsList[k + 1] == words[i - 1]:
                        count += 1
                matrix[i][j] = count
    
    return matrix

text = ""
matrix = co_occurrence(text)
for row in matrix:
    print(row)