import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    # Implementing vectors e,s as lists (arrays) of length 26
    # with p[0] being the probability of 'A' and so on
    e = [0]*26
    s = [0]*26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            # strip: removes the newline character
            # split: split the string on space character
            char, prob = line.strip().split(" ")
            # ord('E') gives the ASCII (integer) value of character 'E'
            # we then subtract it from 'A' to give array index
            # This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char)-ord('A')] = float(prob)
    f.close()

    return (e, s)


def shred(filename):
    '''
    This function takes in a file and "shreds" it by counting the number of times each letter is found
    returns a sorted dict letter_counts which contains capitalized letters as keys and number of times 
    they were found as values
    '''

    # Using a dictionary here. You may change this to any data structure of
    # your choice such as lists (X=[]) etc. for the assignment
    with open(filename, encoding='utf-8') as f:
        # TODO: add your code here

        # list of all letters in alphabet to match up with dict
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # copying entire text to uppercase for ease of use
        # creation of letter_counts
        text = f.read().upper()
        letter_counts = {}

        # for loop to parse through text and increment for every found letter
        for letter in text:
            # if statement to make sure we ignore none alphabetical characters
            if letter.isalpha():
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

        # addition of letters not in the text
        for i in range(0, 25):
            if alphabet[i] not in letter_counts:
                letter_counts[alphabet[i]] = 0

    # sorting of dict
    myKeys = list(letter_counts.keys())
    myKeys.sort()
    sorted_dict = {i: letter_counts[i] for i in myKeys}
    letter_counts = sorted_dict

    # writing output into stdout
    print("Q1\n")
    for letter, count in letter_counts.items():
        print(f"{letter} {count}")
    return letter_counts


# local variable holding return value of shred
idk = {}
idk = shred("letter2.txt")


def baye(d):
    '''
    This function takes in a dict d and returns F(English) and F(Spanish)
    '''
    #2D array of probabilities
    e = get_parameter_vectors()

    #F(English) and F(Spanish)
    result1 = d['A'] * math.log(e[0][0])
    result2 = d['A'] * math.log(e[1][0])

    #output
    print("%.4f" % result1)
    print("%.4f" % result2)


print("Q2")
baye(idk)

#variables to hold F(English) and F(Spanish) respectively
result_e = 0
result_s = 0

#array of keys in dict
keys = list(idk.keys())

e = get_parameter_vectors()

#for loop to compute F(English) and F(Spanish)
for i in range(0, 25):
    result_e += idk[keys[i]] * math.log(e[0][i])
    result_s += idk[keys[i]] * math.log(e[1][i])
result_e += math.log(0.6)
result_s += math.log(0.4)
#output
print("Q3")
print("%.4f" % result_e)
print("%.4f" % result_s)

#variable to hold  P(Y = English | X)
given_e = 0

#if else block to compute  P(Y = English | X)

#if F(Spanish) - F(English) >= 100, set  P(Y = English | X) to 0
if ((result_s - result_e) >= 100):
    given_e = 0

#if F(Spanish) - F(English) <= -100, set  P(Y = English | X) to 1
elif ((result_s - result_e) <= -100):
    given_e = 1

#else compute P(Y = English | X) as given in assignment write up
else:
    given_e = 1 / (1 + math.exp(result_s - result_e))

#output
print("Q4")
print("%.4f" % given_e)
# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
