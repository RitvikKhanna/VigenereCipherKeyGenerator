# Assignment 7 P1 CMPUT 299 Win2018
# Bisan Hasasneh (1505703) and Ritvik Khanna (1479093)
# This cracks the key of a vigenere cipher given its length
# using index of mutual coincidence
#
# the function getNthSubkeysLetters is taken from Hacking Secret Ciphers
# with Python by Al Sweigert http://inventwithpython.com/hacking


import math,sys,random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

    # For testing purposes only
    #message = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    message = "nsydheidgptizqrxefvrykxwfsgtsztwfflalkgvnwlcbwssmotsxctjrqiezwowrygqoeewniftrqgfqmzoaniysqtgubrdexsfxedyremzunngaiaemzu"

    key = vigenereSolver(message,5)
    print(key)
    


# Gets the final key for decryption
def vigenereSolver(ciphertext, keyLength):

    # Empty key initially
    key = ''

    ciphertext = upperAndLetters(ciphertext)

    # Loop in the range of the length of the key to get the key
    for i in range(1,keyLength+1):

        # Get the corresponding sub string for the key position
        subString = getNthSubkeysLetters(i, keyLength, ciphertext)

        # Empty dictionary for every position of the key
        IMC = {}

        # Example: For first position of the key
        # The IMC dict will have some values for every letter in the English alphabet.
        for symbol in LETTERS:

            IMC[symbol] = getIMC(subString)

            subString = shiftBack(subString)

        # Get the letter which has the maximum IMC in the IMC dictionary and add it to the key on that position
        key += getMax(IMC)
 
    # Return the final key
    return(key)
                

    
# This function returns the IMC for the passed sub string
def getIMC(subString):

    # Taken from http://inventwithpython.com/hacking/chapter20.html - freqAnalysis.py
    englishLetterFreq = {'E': 0.1270, 'T': 0.0906, 'A': 0.0817, 'O': 0.0751, 'I': 0.0697, 'N': 0.0675, 'S': 0.0633, 'H': 0.0609, 'R': 0.0599, 'D': 0.0425, 'L': 0.0403,
                         'C': 0.0278, 'U': 0.0276, 'M': 0.0241, 'W': 0.0236, 'F': 0.0223, 'G': 0.0202, 'Y': 0.0197, 'P': 0.0193, 'B': 0.0129, 'V': 0.0098, 'K': 0.0077,
                         'J': 0.0015, 'X': 0.0015, 'Q': 0.0010, 'Z': 0.0007}
    
    # Taken from http://inventwithpython.com/hacking/chapter20.html - freqAnalysis.py
    letterFreq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
                   'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0 }

    # For calculating relative frequency
    letterSum = 0

    # For the IMC
    sumIMC = 0
    
    
    # First get the letter count of all the letters in the sub string
    # This function was taken from http://inventwithpython.com/hacking/chapter20.html - freqAnalysis.py but some variables were changed.
    for letter in subString.upper():
        if letter in LETTERS:
            letterSum += 1
            letterFreq[letter] += 1

    # Editing the list with so that the letters are the key and the corresponding values are the relative frequency instead of their count.
    for key in letterFreq:
        letterFreq[key] = (letterFreq[key]/letterSum)

    # Loop through all the keys and get the IMC which is the sum from A-Z of the relativefrequency times the corresponding english letter frequency
    for key in letterFreq:
        sumIMC += letterFreq[key]*englishLetterFreq[key]

    # Return the IMC
    return sumIMC


# Return the key for the maximum IMC in the IMC dictionary for the corresponding position of the key
def getMax(dictIMC):

    # Initializing
    maxIMC = 0

    # For every key in the passed dictionary search the key with the maximum value and then return that key
    for key in dictIMC:
        if(maxIMC<dictIMC[key]):
            maxIMC = dictIMC[key]
            maxKEY = key

    return(maxKEY)


# Shift back the string as mentioned in the assignment since the substring is nothing but a caesar cipher now.
def shiftBack(string):

    # New shifted empty sub string
    newString = ''

    # For every letter in the sub string passed we find the index and if its out of the range then add 26
    # Then add the corresponding letter with that index to the new string and return it
    for letter in string:
        i = LETTERS.index(letter)-1

        if(i<0):
            i = i + 26

        newString += LETTERS[i] 

    return newString

# Remove all non-letters and change it to uppercase and return the new changed ciphertext
def upperAndLetters(message):

    cipher = ''
    message = message.upper()
    for symbol in message:

        if symbol in LETTERS:
            cipher += symbol

    return(cipher)        



# Taken from http://inventwithpython.com/hacking/chapter20.html - vigenereHacker.py
def getNthSubkeysLetters(n, keyLength, message):
    # Returns every Nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'


    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength

    letters = ''.join(letters)
    
    return(letters)

    

    

if __name__ == '__main__':
            main()


                               
