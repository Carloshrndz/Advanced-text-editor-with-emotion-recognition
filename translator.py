from googletrans import Translator, LANGUAGES

# Initialization of the translator
translator = Translator()

'''
Detects the language of the input text.

Input:
- pText (str)

Output:
- The detected language code of the input text.

Constraints:
- The input text must be a non-empty string.
'''
def detectLanguage(pText):
    try:
        detection = translator.detect(pText)
        return detection.lang
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None

'''
Function to translate the text.

Input:
- pText (str)
- targetLanguage (str)

Output:
- translatedText (str)
The text translated into the specified target language.

Constraints:
- The input text must be a non-empty string.
- The targetLanguage must be a valid language code according to the googletrans library.
'''
def translateText(pText, targetLanguage):
    try:
        translation = translator.translate(pText, dest=targetLanguage)
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None

text = input("Enter the text you want to translate: ")
targetLanguage = input(f"Enter the language code of the target language (example: 'es' for Spanish): ")

if targetLanguage not in LANGUAGES:
    print(f"Target language '{targetLanguage}' is not valid.")
else:
    initialLanguage = detectLanguage(text)
    if initialLanguage:
        print(f"Detected language: {initialLanguage}")

        translatedText = translateText(text, targetLanguage)
        if translatedText:
            print(f"Translated text: {translatedText}")
        else:
            print("Failed to translate text.")
    else:
        print("Failed to detect the language of the text.")
