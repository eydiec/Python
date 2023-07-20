"""
File: anagram.py
Name: Eydie Cheng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO: to list down all the words generated from the word input
    """
    start = time.time()
    ####################
    print('Welcome to stanCode \'Anagram Generator\' (or -1 to quit) ')

    vocabulary = input('Find anagrams for: ')
    length = len(vocabulary)
    read_dictionary()
    found_lst = []
    while vocabulary != EXIT:
        find_anagrams(vocabulary, length, found_lst)
        print(f'{len(found_lst)} anagrams: {found_lst}')
        found_lst = []
        vocabulary = input('Find anagrams for: ')

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def find_anagrams(s, length, found_lst):
    """
    :param s:
    :param length: to get the length of input
    :param found_lst: the collection of words
    """
    dictionary = read_dictionary()
    ans = ''

    find_anagrams_helper(ans, s, length, found_lst, dictionary)


def find_anagrams_helper(ans, vocabulary, length, found_lst, dictionary):
    if len(ans) == length:
        if ans in dictionary:
            if ans not in found_lst:
                print('Searching...')
                print(f'Found: {ans}')

                found_lst.append(ans)


    else:

        for i in range(len(vocabulary)):
            # choose
            ans += vocabulary[i]

            # explore
            if has_prefix(ans, dictionary):
                find_anagrams_helper(ans, vocabulary[:i] + vocabulary[i + 1:], length, found_lst, dictionary)

            # unchoose
            ans = ans[:-1]


def read_dictionary():
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())
    return dictionary


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: based on current input vocabulary
    :param dictionary: to check whether it exists in
    :return: if the search shall continue
    """
    for ans in dictionary:
        if ans.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
