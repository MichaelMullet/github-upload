# Caesar Cipher
import string

def caesarCipher(message, key):
    mode = 'decrypt'
    SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + '1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex <0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol
    return translated

print(caesarCipher('guv6Jv6Jz!J6rp5r7Jzr66ntrM', 13))