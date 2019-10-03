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

    if (len(sys.argv) != 3):
        print("Usage: ./caesar_ciper -o[options] input.txt")
        print("Options: -e [encrypt] or -d [decrypt]")
        exit()

    input_file = open(sys.argv[2], 'r')
    string = input_file.read()
    

    if (sys.argv[1] == '-e'):
        encrypt_output = open("caesar_output_encrypt.txt", "w")
        for i in range(26):
            encrypt_output.write(encrypt(string, i) + '\n')
        encrypt_output.close()

    if (sys.argv[1] == '-d'):
        decrypt_output = open("caesar_output_encrypt.txt", "w")        
        for i in range(26):
            decrypt_output.write(decrypt(string, i) + '\n')
        decrypt_output.close()

    input_file.close()

if __name__ == '__main__':
    main()