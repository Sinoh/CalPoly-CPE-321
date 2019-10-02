import math
import sys

def main():
    array = []
    freq = []

    if (len(sys.argv) != 2):
        print("Usage: ./digraph.py input.txt\n")
        exit()

    input_file = open(sys.argv[2], 'r')
    string = input_file.read()
    
    for i in range(len(string) + 1):
        letters = string[i - 1] + string[i]
        if (letters) in freq:
            freq[freq.index(letters)] += 1
        else:
            array.append(letters)
            freq.append(1)


        

if __name__ == "__main__":
    main()
