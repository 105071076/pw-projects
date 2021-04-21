"""
File: largest_digit.py
Name: Peggy
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: an integer the user inputs
	:return: the largest digit
	"""
	if n < 0:
		n = n * -1
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(digit_left, digit_max):

	# Base case
	if digit_left % 10 == 0:
		if digit_left != 0:
			digit_max = digit_left
		return digit_max

	else:
		if digit_left % 10 > digit_max:
			digit_max = digit_left % 10
			return find_largest_digit_helper(digit_left, digit_max)

		else:
			return find_largest_digit_helper(digit_left // 10, digit_max)



if __name__ == '__main__':
	main()
