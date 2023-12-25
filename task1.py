from __future__ import annotations

"""
Programming Task #1
Given a list of digits, determine the integer that it represents.

For example, given the list: [8,3,5,1], your program should output 8351 as an integer.
"""


def list_to_integer(list: list[int]) -> None:
    """
    This function takes a list of digits and returns the combination of each digit into an integer.

    :param list: a list of integers
    :return: None
    """
    # Initialize an empty string
    result = ""

    # loop through each element in the list
    for num in list:  # we are using for loop since we know the context of the list
        # add each string element to the previous empty result in each iteration
        result += str(num)

    # convert the string result to an integer and return it after the loop is finished
    return int(result)


if __name__ == "__main__":
    example_list = [8, 3, 5, 1]
    result_integer = list_to_integer(example_list)
    print(result_integer)
