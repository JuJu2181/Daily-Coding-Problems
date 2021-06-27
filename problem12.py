"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

#for steps 1 or 2 the problem is fibonacci series so implmented using recursion
def findPossibleWaysFib(n):
    #base case
    return n if n <=1 else findPossibleWaysFib(n-1) + findPossibleWaysFib(n-2)

#for another steps input from user we use another function with similar concept of fiboanacci series 
def findPossibleWays(n,possible_steps):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        possible_ways = 0
        for i in possible_steps:
            possible_ways += findPossibleWays(n - i,possible_steps)
        return possible_ways

def main():
    no_of_steps = int(input("Enter the no of steps in staircase: "))
    possible_steps = set(map(int, input("Enter Possible Steps: ").split()))
    # if possible_steps == {1, 2} or possible_steps == {2, 1}:
    #     print(findPossibleWaysFib(no_of_steps+1))
    # else:
    #     print("To be implemented")

    print(f'Total Possible Unique Ways: {findPossibleWays(no_of_steps+1,possible_steps)}')
    
if __name__ == "__main__":
    main()