

def caesar_encode(plain_text, shift):
    cipher_text = ''
    for c in plain_text:
        caesar_encode = ord(c) + shift
        caesar_encode = chr(caesar_encode)
        cipher_text += caesar_encode
    return cipher_text

    