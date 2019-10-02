import math
import sys

def main():
    freq = [0] * 26

    if (len(sys.argv) != 2):
        print("Usage: ./letterfreq.py input.txt\n")
        exit()

    input_file = open(sys.argv[2], 'r')
    string = input_file.read()
    
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            freq[ord(char) - 65] += 1
        elif (char.islower()):
            freq[ord(char) - 97] += 1
        else:
            continue

if __name__ == "__main__":
    main()
