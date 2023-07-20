"""
File: largest_digit.py
Name: Eydie Cheng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
	:param n: the number of the largest digit
	:return: the largest digit
	"""
    if n < 0:
        n *= -1
    return find_largest_digit_helper(n, -float('inf'))


def find_largest_digit_helper(n, max_num):
    if n == 0:
        return max_num
    else:
        number = n % 10
        if number > max_num:
            max_num = number

        return find_largest_digit_helper(n // 10, max_num)

    # if n%10 == 0:
    # 	pass
    # elif n%10 > max_num:
    # 	return n%10
    # else:
    # 	return max_num


if __name__ == '__main__':
    main()
