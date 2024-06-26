from openai import OpenAI
from k import getOpenAIApiKey

api_key = getOpenAIApiKey()

'''
Generates a list of synonyms and antonyms for the word entered by the user.

Inputs:
- pWord (str)

Output:
- response (str)
(The correction made by the GPT-4o model from OpenAI).

Constraints:
- pWord must be a valid string.
- An internet connection is required to communicate with the OpenAI API and use the GPT-4o model.
'''

def synonymsAndAntonyms(pWord):
    client = OpenAI(api_key=api_key)
    
    messages = [
        {"role": "system", "content": "You are a synonym and antonym finder and follow this format in your response:\n[Synonym]\n-\n-\n-\n[Antonym]\n-\n-\n-."},
        {"role": "user", "content": pWord}
    ]
    messages.append({"role": "user", "content": pWord})
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    response = completion.choices[0].message.content
    
    return response
