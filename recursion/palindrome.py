#!/usr/bin/python3
"""
Check if a string is a palindrome
"""


def palindrome(s):
    # Check if a string is a palindrome
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return palindrome(s[1:-1])

if __name__ == '__main__':
    print(palindrome('lsdkjfskf'))
    print(palindrome('radar'))
    print(palindrome('amanaplanacanalpanama'))
