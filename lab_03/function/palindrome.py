def palindrome(s):
    q = s[::-1]
    if s == q:
        return True
    return False

s = input()
print(palindrome(s))
