def isPalindrome(s):
    rev = ''.join(reversed(s))
    if rev == s:
        return "Palindrome"
    return "Not Palindrome"

s = input()
print(isPalindrome(s))