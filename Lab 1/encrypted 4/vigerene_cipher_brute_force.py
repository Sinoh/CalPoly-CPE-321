import sys
import math
from itertools import product

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
        if (string.isupper()):
            decryption += chr((ord(string[i]) - ord(key[j % len(key)]) + 26) % 26 + 65)
        elif (string.islower()):
            decryption += chr((ord(string[i]) - ord(key[j % len(key)]) + 26) % 26 + 97)
        else:
            decryption += string[i]
            j -= 1
        j+= 1

    return decryption


def main():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    
    if (len(sys.argv) != 4):
        print("Usage: ./vigerene_ciper [Options1] [Options2] input.txt\n")
        print("Options1: -e [encrypt] or -d [decrypt]")
        print("Options2: [key as string] or [ None or key length as int]")
        exit()

    input_file = open(sys.argv[3], 'r')
    string = input_file.read()
    

    if (sys.argv[1] == '-e'):
        encrypt_output = open("vigerene_output_encrypt.txt", "w")
        encrypt_output.write(encrypt(string, sys.argv[2]) + '\n')
        encrypt_output.close()

    if (sys.argv[1] == '-d'):
        decrypt_output = open("vigerene_output_decrypt.txt", "w")
        key_length = int(sys.argv[2])
        if (key_length == None):
            key_length = len(string)

            for length in range(key_length + 1):
                for combo in product(alphabets, repeat = length):
                    key = ''.join(combo)
                    decrypt_output.write(decrypt(string, key) + '\n')
                print((length/26) * 100, '%')
        else:
            count = 0
            for combo in product(alphabets, repeat = key_length):
                key = ''.join(combo)
                decrypt_output.write("key: " + key)
                decrypt_output.write(decrypt(string, key) + '\n')
                count += 1
                percent = count/pow(26, key_length) * 100
                if (percent % 1):
                    print('%0.2f' %(percent), '%')

                


        decrypt_output.close()

    input_file.close()


if __name__ == '__main__':
    main()