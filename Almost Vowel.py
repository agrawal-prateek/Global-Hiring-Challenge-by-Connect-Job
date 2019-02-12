"""
------------------------------------------------------Almost Vowel------------------------------------------------------

You are given with a string S. Your task is to remove atmost two substrings of any length from the given string S
such that the remaining string contains vowels('a','e','i','o','u') only. Your aim is the maximise the length of the
remaining string. Output the length of remaining string after removal of atmost two substrings.
NOTE: The answer may be 0, i.e. removing the entire string.

INPUT FORMAT:

First line of input contains number of test cases T.
Each test case comprises of a single line corresponding to string S.

OUTPUT FORMAT:

Output a single integer denoting length of string containing only vowels after removal of atmost two substrings of any
length.

CONSTRAINTS:

1<=T<=100
1<=|S|<=10^5
S[i]=lowercase characters

Sample Input
2
earthproblem
letsgosomewhere

Sample Output
3
2

Explanation
For the first test case, the maximum length possible is 3. String of length 3 with only vowels formed by removing atmost
2 substrings can be: "eao" or "eae".
For the second test case, the maximum length possible is 2. String of length 2 with only vowels formed by removing
atmost 2 substrings can be: "ee" or "oe".

"""


def find_almost_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    big_number = 0
    left_length = 0
    right_length = 0
    for character in string:
        if character in vowels:
            left_length += 1
        else:
            break
    if left_length == len(string):
        return len(string)
    for index in range(len(string) - 1, -1, -1):
        if string[index] in vowels:
            right_length += 1
        else:
            break
    string = string[left_length:len(string) - right_length]
    temp_big = 0
    for character in string:
        if character in vowels:
            temp_big += 1
        else:
            if temp_big > big_number:
                big_number = temp_big
            temp_big = 0
    if temp_big > big_number:
        big_number = temp_big
    return big_number + left_length + right_length


t = int(input())
for _ in range(t):
    print(find_almost_vowel(input()))
