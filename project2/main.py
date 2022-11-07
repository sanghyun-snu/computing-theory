import sys
import string
import random

def inputfile_generator():
    f1 = open("./1.in", "w")
    f2 = open("./2.in", "w")
    
    rnd1 = input_generator(1000)
    rnd2 = input_generator(100000)
    
    f1.write(rnd1)
    f2.write(rnd2)
    
    f1.close()
    f2.close()

    return

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
        dictionary[c] = index
        index += 1
    
    return dictionary


def compression(input, dictionary):
    en_dict = dictionary
    print(en_dict)
    encoded = []
    w = "" # init string
    for c in input:
        if w + c in en_dict:
            w = w + c
        else:
            # dict code for w to output
            encoded.append(en_dict[w])
            # add (w + c) to dict
            en_dict[w+c] = len(en_dict) + 1
            w = c
    # add last character
    encoded.append(en_dict[w])
    # for i in input:

    return en_dict, encoded
def uncompression(input):
    decoded = []
    
    return decoded

def main():
    # argument parsing
    args = sys.argv
    version = int(args[1]); inputfile = str(args[2]); outputfile = str(args[3])

    input = open(inputfile, "r")
    output = open(outputfile, "w")

    # make dictionary for encoding
    dictionary = alphabets()

    if version == 1:
        en_dict, encoded = compression(input.read(), dictionary)
    if version == 2:
        de_input = uncompression(input.read(), )
    

    # write the output
    output.write(str(en_dict))
    output.write("\n")
    output.write(str(encoded))

    # close the file object
    input.close()
    output.close()
if __name__ == "__main__":
    # dictionary = alphabets()
    # file_generator()
    # rnd = input_generator(100)
    main()
