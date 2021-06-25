"""
# Day 9
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def findLargestNonAdjacentSum(input_list):
    sum1 = 0
    for j in range(2,len(input_list)):
        # j will be the step 
        tempSum = 0
        #  we need to find sum of all the non adjacent integers that differ by different steps
        for i in range(0,len(input_list),j):
            tempSum += input_list[i]
        if tempSum > sum1:
            sum1 = tempSum
    return sum1 if sum1 > 0 else 0

def findLargestSum(input_list):
    if len(input_list) <= 2:
        return max(input_list)
    sum1 = 0
    tempSum = input_list[0]
    for i in range(2,len(input_list)):
        sum1,tempSum = tempSum + input_list[i], max(sum1,tempSum)
    return max(sum1,tempSum)


def main():
    input_list = list(map(int,input('Enter the list of integers: ').split()))
    # in O(n2)
    print(f'Largest Non Adjacent Sum is {findLargestNonAdjacentSum(input_list)}')
    # print(f'Largest Non Adjacent Sum is {findLargestSum(input_list)}')

if __name__ == "__main__":
    main()