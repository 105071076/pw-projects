"""
File: boggle.py
Name: Peggy
----------------------------------------
TODO: create a boggle game by using back tracking method.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
import time
FILE = 'dictionary1.txt'
read_dic = {}


def main():
	"""
	TODO:
	"""

	all_char = []

	for i in range(4):
		print((i+1), ' row of letters: ', end='')
		char = input()
		if len(char) != 7 or num_there(char) is True:
			print('Illegal Input')

		all_char.append(char.split())

	start = time.time()
	result = find_word(all_char,'',[])
	end = time.time()
	print('There are ', len(result), ' words in total.')
	print('Process time: %f seconds ' % (end - start))


def num_there(s):
	# s is the string the user inputs
	digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	for num in digit:
		if str(num) in s:
			return True
		else:
			return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global read_dic
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				read_dic[word] = word
	return read_dic


def find_word(all_char,sub_str,result):
	"""
	:param all_char: the list that saves the characters the user input
	:param sub_str: the substring of the word
	:param result: save the words that are matched in the dictionary
	:return: the result list
	"""

	global read_dic
	read_dictionary()
	for y in range(len(all_char)):
		for x in range(len(all_char)):
			first_x = x
			first_y = y
			option_ls = [(first_x, first_y)]
			sub_str += all_char[first_x][first_y]  # add the letters into substring
			find_word_helper(first_x, first_y, sub_str, all_char,option_ls,result)
			option_ls.pop()
			sub_str = sub_str[:len(sub_str)-1]  # give away the last letter

	return result


def find_word_helper(first_x, first_y, sub_s, all_char,option_ls,result):
	"""
	:param first_x: the order of the row
	:param first_y: the order of the letter in the chosen row
	:param sub_s: the substring of the word
	:param all_char: the list that saves the characters the user input
	:param option_ls: the list that saves the characters near the start point
	:param result: save the words that are matched in the dictionary
	"""
	global read_dic
	if len(sub_s) >= 4:
		if sub_s in read_dic:
			if sub_s not in result:
				print('Found', sub_s)
				result.append(sub_s)

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			char_x = first_x + i
			char_y = first_y + j
			if 0 <= char_x < 4:
				if 0 <= char_y < 4:
					if (char_x,char_y) not in option_ls:
						option_ls += [(char_x,char_y)]
						sub_s += all_char[char_x][char_y]
						if has_prefix(sub_s) is True:
							find_word_helper(char_x, char_y, sub_s, all_char,option_ls,result)
							sub_s = sub_s[:len(sub_s)-1]  # give away the last letter
							# go back to the first letter
							char_x -= i
							char_y -= j
							option_ls.pop()

						else:
							sub_s = sub_s[:len(sub_s)-1]
							char_x -= i
							char_y -= j
							option_ls.pop()


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global read_dic
	for key, value in read_dic.items():
		if value.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
