
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    i=0
    for letter in plaintext:

        #upper case
        if (letter.isupper()):
            ciphertext += chr((ord(letter) + key-65) % 26 + 65)

        #lower case
        else:
             ciphertext += chr((ord(letter) + key - 97) % 26 + 97)

    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    i=0
    for letter in ciphertext:

        #upper case
        if (letter.isupper()):
            plaintext += chr((ord(letter) - key-65) % 26 + 65)

        #lower case
        else:
             plaintext += chr((ord(letter) - key -97) % 26 + 97)
    return "abc"


