'''
convertTextToSpeech(pText, pEmotion):
Input:
- pText (Str)
- pEmotion (Str)
Output:
- engine.runAndWait(); to execute the speech synthesis.
Restrictions:
- The voice used is specific to Windows. This needs to be adjusted in another platform or if you don't have installed the voice.
'''
def convertTextToSpeech(pText, pEmotion = ''):
    import pyttsx3
    rate, volume, pitch = getEmotionConfig(pEmotion)
    engine = pyttsx3.init()
    
    engine. setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.setProperty('pitch', pitch )
    
    engine.say(pText)
    
    return engine.runAndWait()


'''
getEmotionConfig(pEmotion):
Input:
- pEmotion (Str)
Output:
- rate (int)
- volume (volume)
- pitch (int)
Restrictions:
- pEmotion == 'joy' | 'love' | 'anger' | 'sadness' | 'surprise' | 'confusion' | 'affection' | 'frustration' | 'atonishment'
'''
def getEmotionConfig(pEmotion):
    if pEmotion == 'joy':            return 180, 1.0, 2
    elif pEmotion == 'love':         return 150, 0.8, 1
    elif pEmotion == 'anger':        return 190, 1.2, 0
    elif pEmotion == 'sadness':      return 110, 0.8, -1
    elif pEmotion == 'surprise':     return 220, 1.0, 3
    elif pEmotion == 'confusion':    return 110, 0.9, 0
    elif pEmotion == 'affection':    return 160, 0.9, 1
    elif pEmotion == 'frustration':  return 200, 1.2, 0
    elif pEmotion == 'astonishment': return 210, 1.0, 2
    else:                            return 150, 1.0, 0