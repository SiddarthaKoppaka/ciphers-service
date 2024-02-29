# def caesar_encode(plain_text, shift):
#     cipher_text = ''
#     for c in plain_text:
#         c_encoded = ord(c) + shift
#         c_encoded = chr(c_encoded)

#         cipher_text += c_encoded    
#     return cipher_text

# updated encode function
def caesar_encode(plain_text, shift):
    cipher_text = ''
    for c in plain_text:
        if c.isalpha():  # Check if the character is alphabetic
            base = ord('a') if c.islower() else ord('A')  # Determine the base value for lowercase or uppercase
            c_encoded = chr((ord(c) - base + shift) % 26 + base)  # Apply the shift with wraparound
        else:
            c_encoded = c  # Keep non-alphabetic characters unchanged

        cipher_text += c_encoded
    return cipher_text
