import sys
import string
import random

def input_generator(size):
    # make alphabet sum list
    english = string.ascii_letters
    digits = string.digits
    special = "?! ,.:;\n"
    all_sum = english + digits + special

    # make random string with given size
    rnd_string = ''.join(random.choice(all_sum) for _ in range(size))
    return rnd_string

def alphabets():
    # make alphabet sum list
    english = string.ascii_letters
    digits = string.digits
    special = "?! ,.:;\n"
    all_sum = english + digits + special
    
    # init index and dict
    index = int(1)
    dictionary = {}

    # make dict
    for c in all_sum:
        dictionary[index] = c
        index += 1
    
    return dictionary, index


def compression(input, dictionary, idx):

    return en_dict, en_input
def uncompression():
    return 
def main():
    # argument parsing
    args = sys.argv
    version = int(args[1]); inputfile = str(args[2]); outputfile = str(args[3])

    input = open(inputfile, "r")
    output = open(outputfile, "w")

    # make dictionary for encoding
    dictionary, idx = alphabets()

    if version == 1:
        en_dict, en_input = compression(input, dictionary, idx)
    if version == 2:
        de_input = uncompression(en_dict)
    
    # write the output


    # close the file object
    input.close()
    output.close()
if __name__ == "__main__":
    # dictionary, index = alphabets()
    # rnd = input_generator(100)
    # main()
