#!/usr/bin/env python

# I forgot my phone PIN, but knew the digits I used.
# Use './pin.py 1 2 3 4' to return all permutations 
# of 4 digits.

import sys
from itertools import permutations

def get_input_list():
    input_list = [
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]]
    
    return input_list

def main():
    for permutation in permutations(get_input_list()):
        print ("".join(i for i in permutation))

if __name__ == "__main__":
   main()
