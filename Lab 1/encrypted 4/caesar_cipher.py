import math
import sys

def encrypt(string, shift):
    encryption = ""

    for i in range(len(string)):
        char = string[i]

        if (char.isupper()):
            encryption += chr((ord(char) - 65 + shift) % 26 + 65)

        else:
            encryption += chr((ord(char) - 97 + shift) % 26 + 97)
    
    return encryption

def decrypt(string, shift):
    decryption = ""

    for i in range(len(string)):
        char = string[i]

        if (char.isupper()):
            decryption += chr((ord(char) - 65 - shift) % 26 + 65)

        elif(char.islower()):
            decryption += chr((ord(char) - 97 - shift) % 26 + 97)
        
        else:
            decryption += char
    
    return decryption

def main():
    input_file = open(sys.argv[1], 'r')
    encryption = input_file.read()
    encryption = encryption.lower()


    for i in range(26):
        print(decrypt(encryption, i) + '\n')

if __name__ == '__main__':
    main()