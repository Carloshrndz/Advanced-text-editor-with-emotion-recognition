def interpretEmoticons(pText):
    '''
    Detects and classifies emoticons in the text.

    Input:
    - pText (str)

    Output:
    - scores (dict):

    Restrictions:
    - The input text must be a non-empty string.
    '''
    emoticons = {
        "Joy": [":)", ":-)", ":D", ":-D", ":))", ":-))"],
        "Sadness": [":(", ":-(", ":'(", "T_T", ":’(", ":’("],
        "Surprise": [":O", ":-O", ":o", ":-o", ":0", ":-0"],
        "Anger": [">:(", ">:O", "D:<"],
        "Love": ["<3", "<3<3", ":-*", ":*", ":-X", ":X"],
        "Amazement": [":", ":-0", ":O", ":-O", "O.O", "o.O"],
        "Affection": [":)", "^^", "^_^", "<('.'<)", "(>'.')>", "<3"],
        "Confusion": [":/", ":-/", ":?", ":-?", "o.O", "O.o"],
        "Frustration": [":(", ":-(", ":/", ":-/", ":((", ":-(("]
    }

    emotions = {category: 0 for category in emoticons.keys()}
    for category, emoticonList in emoticons.items():
        for emoticon in emoticonList:
            if emoticon in pText:
                emotions[category] += 1
    totalEmoticons = sum(emotions.values())
    scores = {category: count / totalEmoticons for category, count in emotions.items()}
    return scores