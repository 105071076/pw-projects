"""
File: anagram.py
Name: Peggy
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
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_list = []


def main():
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')

    while True:
        s1 = [] # save the characters that will be checked
        s = input('Find anagrams for: ')
        for ele in s:
            s1.append(ele)
        read_dictionary(len(s), s1)
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s,s1)
            end = time.time()
            print('Process time: %f seconds ' % (end-start))


def read_dictionary(num,s1):
    """

    :param num: the length of s
    :param s1: a list that saves the characters that will be checked
    :return: a wordlist that saves only the the word that has the same length with s
            and the ones that starts with the same character
    """
    global word_list
    word_list = []
    with open(FILE,'r') as f:
        for line in f:
            word = line.strip()
            for ele in s1:
                # only append the word that has the same length with s and the ones that starts with the same character
                if len(word) == num and word.startswith(ele):
                    word_list.append(word)
    return word_list


def find_anagrams(s,s1):
    """
    :param s: the string the user inputs
    :param s1: a list that saves the characters that will be checked
    :return: the words that appears in the dictionary
    """
    global word_list
    print('Searching...')
    for i in range(len(find_anagrams_helper(s,[],s1,[]))):
        print('Found: ',find_anagrams_helper(s,[],s1,[])[i],'\nSearching...')
    print(len(find_anagrams_helper(s,[],s1,[])), 'anagrams: ',find_anagrams_helper(s,[],s1,[]) )


def find_anagrams_helper(s,word_in_dic,s1,s2):
    """

    :param s: the string the user inputs
    :param word_in_dic: a list that saves the correct words appeared in the dictionary
    :param s1: a list that saves the characters that will be checked
    :param s2: saves the substring
    :return: word_in_dic
    """
    global word_list

    if len(s2) == len(s):
        s2 = ''.join(s2)
        if s2 in word_list and s2 not in word_in_dic:
            word_in_dic.append(s2)
    else:
        for i in range(len(s1)):
            if has_prefix(s2):
                ele = s1.pop(i)
                s2.append(ele)
                find_anagrams_helper(s, word_in_dic,s1,s2)
                ele = s2.pop()
                s1.insert(i,ele)

    return word_in_dic


def has_prefix(sub_s):
    """
    :param sub_s: the substring of the string the user inputs
    :return: True or False
    """
    global word_list
    sub_s = ''.join(sub_s)
    for word in word_list:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
