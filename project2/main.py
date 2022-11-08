import sys
import string
import random

from struct import *
MAX_SIZE = pow(2,8)

def inputfile_generator():
    f1 = open("./1.in", "w")
    f2 = open("./2.in", "w")
    
    rnd1 = input_generator(100000)
    rnd2 = input_generator(1000000)
    
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

def alphabets(version):
    # make alphabet sum list
    english = string.ascii_letters
    digits = string.digits
    special = "?! ,.:;\n"
    all_sum = english + digits + special
    
    # init index and dict
    index = int(0)
    dictionary = {}

    # make dict
    if version == 1:
        for c in all_sum:
            dictionary[c] = index
            index += 1
    if version == 2:
        for c in all_sum:
            dictionary[index] = c
            index += 1
        
    return dictionary


def compression(input, dictionary):
    en_dict = dictionary
    encoded = []
    w = "" # init string
    for c in input:
        if w + c in en_dict:
            w = w + c
        else:
            # dict code for w to output
            encoded.append(en_dict[w])
            # add (w + c) to dict
            if len(en_dict) < MAX_SIZE:
                en_dict[w+c] = len(en_dict)
            w = c
    # add last character
    encoded.append(en_dict[w])
    # for i in input:

    return en_dict, encoded
def uncompression(input, dictionary):
    dict_size = 256 # dictionary size
    de_dict = dictionary
    decoded = []
    old = input[0] # first input idx
    s = de_dict[old] # first alphabet
    w = s
    decoded.append(s) # output the first alphabet
    # w = entry 
    for idx in input[1:]:
        if idx in de_dict:
            s = de_dict[idx] # translation of idx
        else:
            s = w + w[0] # translation of old
        decoded.append(s)
        de_dict[len(de_dict)] = w + s[0]
        w = s

    return de_dict, decoded

def main():
    # argument parsing
    args = sys.argv
    version = int(args[1]); inputfile = str(args[2]); outputfile = str(args[3])

    # get file; input and output
    input = None ; output = None

    if version == 1:
        input = open(inputfile, "r")
        output = open(outputfile, "wb")
    if version == 2:
        input = open(inputfile, "rb")
        output = open(outputfile, "w")
    
    # make dictionary for encoding
    dictionary = alphabets(version)
    
    if version == 1:
        en_dict, encoded = compression(input.read(), dictionary)
    if version == 2:
        comp_data = []
        while True:
            rec = input.read(1)
            if len(rec) != 1:
                break
            (data, ) = unpack('>B', rec)
            comp_data.append(data)
        de_dict, decoded = uncompression(comp_data, dictionary)
    # print(len(en_dict))
    # print(len(de_dict))

    # # write the output
    if version == 1:
        for e in encoded:
            output.write(pack('>B', int(e)))
        # init = 0
        # for e in encoded:
        #     if init == 0:
        #         output.write(str(e))
        #         init = 1
        #     else:
        #         output.write("," + str(e))
    
    if version == 2:
        for d in decoded:
            output.write(str(d))

    # close the file object
    input.close()
    output.close()
if __name__ == "__main__":
    # dictionary = alphabets()
    # inputfile_generator()
    # rnd = input_generator(100)
    main()
    # tmp = alphabets(2)
    # print(tmp)