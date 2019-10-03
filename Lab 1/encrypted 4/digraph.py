import math
import sys

def main():
    array = []
    freq = []

    if (len(sys.argv) != 2):
        print("Usage: ./digraph.py input.txt\n")
        exit()

    input_file = open(sys.argv[1], 'r')
    output = open("digraph_output.txt", 'w')
    string = input_file.read()
    string = string.replace('\n','')
    
    for i in range(len(string) - 1):
        if not (string[i].isalpha()) or not (string[i + 1].isalpha()):
            continue
        else:
            letters = string[i] + string[i + 1]
            if (letters) in array:
                freq[array.index(letters)] += 1
            else:
                array.append(letters)
                freq.append(1)
    

    for i in range(len(array)):
        output.write(array[i] + ": " + str(freq[i]) + '\n')
        


        

if __name__ == "__main__":
    main()
