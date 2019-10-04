import sys

def encrypt(string, key):
    encryption = ""
    
    for i in range (len(string)):

        if (string[i].isupper()):
            encryption += chr(key[(ord(string[i]) - 65)] + 65)
        elif (string[i].islower()):
            encryption += chr(key[(ord(string[i]) - 97)] + 97)
        else:
            encryption += string[i]
        
    return encryption

def decrypt(string, key):
    decryption = ""

    for i in range(len(string)):

        if (string[i].isupper()):
            decryption += chr(int(key.index(chr(ord(string[i]) - 65 + 97)) + 65))

        elif (string[i].islower()):
           decryption += chr(int(key.index(chr(ord(string[i]) - 97)) + 97))
        else:
            decryption += string[i]
    
    return decryption

def main():

    if (len(sys.argv) != 4):
        print("Usage: ./vigerene_ciper [Options1] -k[key] input.txt\n")
        print("Options1: -e [encrypt] or -d [decrypt]")
        print("Options2: -k [key]")
        exit()

    input_file = open(sys.argv[3], 'r')
    string = input_file.read()
    output = open("mono_output.txt", 'w')
    
    if (sys.argv[1] == '-e'):
        encrypt_output = open("mono_encrypted_output.txt", "w")
        encrypt_output.write(encrypt(string, sys.argv[2]) + '\n')
        encrypt_output.close()

    if (sys.argv[1] == '-d'):
        decrypt_output = open("mono_decrypted_output.txt", "w")
        decrypt_output.write(decrypt(string, sys.argv[2] + '\n'))
        decrypt_output.close()

    input_file.close()
    output.close()

if __name__ == '__main__':
    main()