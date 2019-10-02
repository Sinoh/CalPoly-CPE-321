import math
import sys

def main():
    if (len(sys.argv) != 2):
        print("Usage: ./chi_squared.py input.txt\n")
        exit()

    input_file = open(sys.argv[2], 'r')
    string = input_file.read()
    

if __name__ == "__main__":
    main()
