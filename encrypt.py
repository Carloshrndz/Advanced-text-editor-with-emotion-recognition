from Crypto.Cipher import AES
import base64

# EncryptAES
'''
Input:
- text(str)
Output:
- codedText(bytes)
- tag(bytes)
- nonce(bytes)
Restrictions
- pText must be a string
'''

def encryptAES(pString):
    key = b'\x1a\xd2\xd3\x0b\xc2\xd2~\xe0\xdf5\xa2\x06V\xa2\x0e\xed'
    code = AES.new(key, AES.MODE_EAX)
    nonce = code.nonce
    try:
        codeText, tag = code.encrypt_and_digest(pString.encode("ascii"))
        return base64.b64encode(codeText).decode('ascii'), base64.b64encode(nonce).decode('ascii'), base64.b64encode(tag).decode('ascii')
    except AttributeError:
        return "Please enter a string"

# DecryptAES
'''
Input:
- codedText(bytes)
- tag(bytes)
- nonce(bytes)
Output:
- plainText(str)
Restrictions:
- codedText must be in bytes
- tag must be in bytes
- nonce must be in bytes
'''

def decryptAES(codedText, nonce, tag):
    key = b'\x1a\xd2\xd3\x0b\xc2\xd2~\xe0\xdf5\xa2\x06V\xa2\x0e\xed'
    code = AES.new(key, AES.MODE_EAX, nonce=base64.b64decode(nonce))
    try:
        plainText = code.decrypt_and_verify(base64.b64decode(codedText), base64.b64decode(tag))
        return plainText.decode("ascii")
    except ValueError:
        return "Key incorrect or message corrupted"

codedText, nonce, tag = encryptAES('Hello world.')

