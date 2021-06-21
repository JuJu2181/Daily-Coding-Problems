"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
def searchForLowestMissingPositiveInteger(input_number,input_array):
    """
    Main Logic:
    Here as we have to find the first missing positive integer in linear time and constant space.
    i-e O(1)
    Linear time means time is independent of the input 
    Constant space means that the memory used doesn't depend on the size of input
    we cannot use iteration process so to avoid linear time I choose recursion
    """
    output_number = input_number if input_number not in input_array else searchForLowestMissingPositiveInteger(input_number+1,input_array)
    return output_number

def main():
    input_array = list(map(int,input("Enter the array of integers: ").split()))
    # here we will start from 1 so it will ignore all negative values as well as zeroes and then start checking if the number is present in array or not from 1
    print(f'Lowest Missing Positive number in given array is {searchForLowestMissingPositiveInteger(1,input_array)}')


if __name__ == "__main__":
    main()