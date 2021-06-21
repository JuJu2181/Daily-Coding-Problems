"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decode(input_code:str)->int:
    if(input_code[0] < '1'):
        return 0
    count = 1
    length_of_code = len(input_code)
    # iterate through the length of string
    for i in range(length_of_code-1):
        """
        Main logic
        If code has length 1 count will be 1
        else
        if current letter in code is 1 or 2 and the next digit is less than7 because max digit is 26 , we will increase the count
        e.g in case of 1234
        for 1 next will be 2 and condition satisfies so count increases 
        count = 2
        for 2 next will be 3 condition satisfies so count increase
        count = 3
        for 3 first condition fails so count is not increased 
        so maximum possible codes is 3
        """
        if((input_code[i] == '1' or input_code[i] == '2') and input_code[i+1]<'7'):
            count +=1
    return count


def main():
    input_code = input('Enter the code to decode: ')
    count = decode(input_code)
    if not (count):
        print("Invalid code")
    else:
        print(f'count of codes = {count}')

if __name__ == "__main__":
    main()