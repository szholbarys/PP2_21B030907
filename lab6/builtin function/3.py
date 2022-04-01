def isPalindrome(s):
    rev = ''.join(reversed(s)) # first we reversed words and joined
    if rev == s:
        return "Palindrome"
    return "Not Palindrome"

s = input()
print(isPalindrome(s))