"""
File: hangman.py
Name: Peggy
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: Play hangman and count the lives.
    """
    ans = random_word()
    intro(ans)
    live_cnt = N_TURNS
    temp_ans = ''
    for i in range(len(ans)):
        temp_ans += '-'
    while True:
        if live_cnt == 0:
            break
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()  # case-insensitive
        if not input_ch.isalpha():
            print("illegal format.")
        else:
            if len(input_ch) != 1:
                print("illegal format.")
            else:
                temp_ans = check(ans,temp_ans,input_ch)
                if temp_ans == ans:
                    print("You are correct!\nYou win!!")
                    print("The word was: "+ans)
                    break
                print("The word looks like " + temp_ans)
                for i in range(7):
                    if ans.find(input_ch) == -1:
                        live_cnt = live_cnt - 1  #
                        if live_cnt != 0:
                            print("There is no " + input_ch + "'s in the word.")
                            print("You have " + str(live_cnt) + " guesses left.")
                        else:
                            print("You are completely hung :(")
                            print("The word was: "+ans)
                        break
                    else:
                        print("You have "+str(live_cnt)+" guesses left.")
                        break


def intro(ans):
    """
    The introduction of the game.
    :param ans: The word to guess. It shows the number of the letters.
    """
    word = ''
    for ch in ans:
        word += '-'
    print('The word looks like: '+word)
    print('You have '+str(N_TURNS)+' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def check(ans, temp_ans, input_ch):
    """
    Check if the user guessed the right letter.
    :param ans: The correct word string.
    :param temp_ans:Every temporarily answer when the user guess a letter.
    :param input_ch: The character the user input.
    :return: return to the temporarily answer when the user do a new guess.
    """
    for i in range(len(ans)):
        if input_ch in ans[i]:
            temp_ans = temp_ans[:i] + ans[i] + temp_ans[i+1:]
    return temp_ans



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if  __name__ == '__main__':
    main()
