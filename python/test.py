## compute_input.py

import sys, json, numpy as np

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return(json.loads(lines[0]))

def main():
    #get our data as an array from read_in()
    input = read_in()
    #print(input)
    output = input['first'] + input['second']
    #return the sum to the output stream
    print(output)

#start process
if __name__ == '__main__':
    main()
