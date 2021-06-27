"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

def checkForString(query_string,string_from_list):
    n1 = len(query_string)
    n2 = len(string_from_list)
    if n1 > n2:
        return False
    elif n1 == n2:
        return True if query_string == string_from_list else False   
    else:
        # using for loop for comparing each character in string
        # for j in range(n1):
        #     if query_string[j] != string_from_list[j]:
        #         return False
        # instead of using loop to compare each character in string we can use slicing
        if query_string == string_from_list[:n1]:
            return True
        return False

def main():
    input_list = input('Input the list of query strings: ').split()
    input_string = input('Input the query string: ')
    output_list = []
    for i in input_list:
        if checkForString(input_string,i):
            output_list.append(i)
    print(f'Output set of strings: {output_list}')


if __name__ == "__main__":
    main()