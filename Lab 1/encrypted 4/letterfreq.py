import sys

def main():
    total_char = 0
    freq = [0] * 26
    if (len(sys.argv) != 2):
        print("Usage: ./letterfreq.py input.txt\n")
        exit()

    input_file = open(sys.argv[1], 'r')
    
    string = input_file.read()
    output = open("char_freq_output.txt", "w") 

    for i in range(len(string)):
        char = string[i]
        if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
            if (char.isupper()):
                freq[ord(char) - 65] += 1
            elif (char.islower()):
                freq[ord(char) - 97] += 1
        else:
            continue
        
    
    for i in range(26):
        total_char += freq[i]
        output.write(chr(i+65) + ': ' + str(freq[i]) + '\n')

    output.write(str(total_char)) 


    
if __name__ == "__main__":
    main()
