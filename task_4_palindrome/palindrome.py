def isPalindrome(input, n, position):
    """
    Checks whether an input string is a palindrome.
    Parameters: 
     - input string to compare (should be either lowercase or uppercase)
     - n length of the input - 1
     - position of character in input from start and end
    """
    # position starts at 0
    i = position
    j = n - position
    # the input is not a palindrome
    if input[i] != input[j]:
        return False
    # base case is i == j or j == 0
    # if we have come so far, the input
    # is a palindrome
    if i == j or j == 0:
        return True
    
    return isPalindrome(input, n, position + 1)


def main():
    test_1 = "gag"
    test_2 = "mum"
    test_3 = "a"
    test_4 = "Abba"
    test_5 = "Great"
    print(f'{test_1} is palindrome ? {isPalindrome(test_1,len(test_1)-1,0)}')
    print(f'{test_2} is palindrome ? {isPalindrome(test_2,len(test_2)-1,0)}')
    print(f'{test_3} is palindrome ? {isPalindrome(test_3,len(test_3)-1,0)}')
    print(f'{test_4} is palindrome ? {isPalindrome(test_4.lower(),len(test_4)-1,0)}')
    print(f'{test_5} is palindrome ? {isPalindrome(test_5,len(test_5)-1,0)}')

if __name__ == "__main__":
    main()
