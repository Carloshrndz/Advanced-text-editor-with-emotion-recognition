import spacy
nlp = spacy.load('en_core_web_sm')
'''
namedEntityRecognition(pTexto):
Input:
- pText (Str)
Output:
- Output (List); List of list with: text, start_char, end_char, label; for every ent in pText
Constraints:
- pText must be an valid string
'''
def namedEntityRecognition(pText):
    output = [] 
    doc = nlp(pText)
    
    for ent in doc.ents:
        output += [[ent.text, ent.start_char, ent.end_char, ent.label_]]
    return output


'''
relationshipRecognition(pText):
Input:
- pText (str)
Output: 
- List of list with subject, verb and object; for every sentence in pText
Constraints:
- pText must be an valid string
'''
def relationshipRecognition(pText):
    doc = nlp(pText)
    subjectList = ['nsubjpass', 'nsubj', 'compound']
    verbList = ['ROOT', 'auxpass', 'aux', 'acl', 'advcl']
    objectList = ['pobj', 'acomp', 'dobj', 'comppound']
    output = []
    for sentence in doc.sents:
        subject = verb = object = ''
        for iToken in range(len(sentence)):
            token = sentence[iToken]
            
            print(token.text+' '+token.dep_)
            
            if token.dep_ in subjectList:
                if sentence[iToken - 1].dep_ == 'det':
                    subject = sentence[iToken - 1].text + ' '
                subject += token.text + ' '

            if token.dep_ in verbList:
                verb += token.text + ' '
                
            if token.dep_ in objectList:
                object += token.text + ' '
            elif object:
                break
        if subject and verb and object:
            output += [[subject[:-1], verb[:-1], object[:-1]]]
    return output

