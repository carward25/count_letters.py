#name: Cassidy Ward
#date: 11/17/2021
#description: this program takes as a parameter a string
# and returns a dictionary that tabulates how many of each letter is in that string

def count_letters(string):
    letter_dic = {}
    #looping through each character in string, converted to upper case to
    #minimise comparisons
    for c in string.upper():
        #checking if c is an alphabet
        if c.isalpha():
            #if c is already in letter_dic, adding 1 to current count
            #note that the syntax is letter_dic[c] += 1 , not letter_dic[c] =+ 1
            if c in letter_dic:
                letter_dic[c] += 1
            #otherwise, adding to dict with count=1
            else:
                letter_dic[c] = 1
    #return the dictionary
    return letter_dic