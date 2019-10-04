import sys
import math


def encrypt(string, key):
    encryption = ""
    j = 0
    
    for i in range (len(string)):

        if (string.isupper()):
            encryption += chr((ord(string[i]) + ord(key[j % len(key)]) - 65) % 26 + 65)
        elif (string.islower()):
            encryption += chr((ord(string[i]) + ord(key[j % len(key)]) - 97) % 26 + 97)
        else:
            encryption += string[i]
            j -= 1
        j += 1
        
    return encryption

def decrypt(string, key):
    decryption = ""
    j = 0
    for i in range(len(string)):
        if (string[i].isalpha()):
            if (string.isupper()):

                decryption += chr((ord(string[i]) - ord(key[j % len(key)]) + 26) % 26 + 65)
            else:
                decryption += chr((ord(string[i]) - ord(key[j % len(key)]) + 26) % 26 + 97)

        else:

            decryption += string[i]
            j -= 1
        j+= 1

    return decryption


def main():

    if (len(sys.argv) != 4):
        print("Usage: ./vigerene_ciper [Options1] [Options2] input.txt\n")
        print("Options1: -e [encrypt] or -d [decrypt]")
        print("Options2: [key as string] or [ None or key length as int]")
        exit()

    input_file = open(sys.argv[3], 'r')
    string = input_file.read()
    
    

    if (sys.argv[1] == '-e'):
        encrypt_output = open("vigenere_encrypted_output", "w")
        encrypt_output.write(encrypt(string, sys.argv[2]) + '\n')
        encrypt_output.close()

    if (sys.argv[1] == '-d'):
        decrypt_output = open("vigenere_decrypted_output.txt", "w")
        decrypt_output.write(decrypt(string, sys.argv[2]) + '\n')
        decrypt_output.close()

    input_file.close()


if __name__ == '__main__':
    main()