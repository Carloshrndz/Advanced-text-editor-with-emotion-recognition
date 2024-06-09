
# pip install pycryptodome
from Crypto.Cipher import AES

# EncryptAES
'''
Input:
- text(str)
Output:
- codedText(bytes)
- tag(bytes)
- nonce(bytes)
Restrictions
-  pText must be a string
'''

def encryptAES(pString):
    key = b'\x1a\xd2\xd3\x0b\xc2\xd2~\xe0\xdf5\xa2\x06V\xa2\x0e\xed'
    code = AES.new(key, AES.MODE_EAX)
    nonce = code.nonce
    try:
        codeText, tag = code.encrypt_and_digest(pString.encode("ascii"))
        return codeText, nonce, tag
    except AttributeError:
        return "Please enter a string"



# DecryptAES
'''
Input:
- codedText(bytes)
- tag(bytes)
- nonce(str)
Output:
- plainText(str)
Restrictions:
- codedText must be in bytes
- tag must be in bytes
- nonce must be in bytes
'''

def decryptAES(codedText, nonce, tag):
    key = b'\x1a\xd2\xd3\x0b\xc2\xd2~\xe0\xdf5\xa2\x06V\xa2\x0e\xed'
    code = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plainText = code.decrypt_and_verify(codedText, tag)
        return plainText.decode("ascii")
    except ValueError:
        return "Key incorrect or message corrupted"


    