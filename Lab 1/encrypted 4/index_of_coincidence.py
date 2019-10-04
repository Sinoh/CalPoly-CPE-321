import sys

def main():
    ic = 0

    if (len(sys.argv) != 2):
        print("Usage: ./index_of_coincidence.py char_freq_output.txt\n")
        exit()

    input_file = open(sys.argv[1], 'r')
    
    string = input_file.read()
    input_file.close()

    string = string.replace(':','').strip().split()
    total_char = int(string[-1])
    
    for i in range(len(string) - 1):
        if (string[i].isdigit()):
            n = int(string[i])
            ic += ((n * (n- 1)) / (total_char * (total_char - 1)))
    
    print('%0.6f' %ic)
    
if __name__ == "__main__":
    main()
