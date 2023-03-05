def reverse(n):
    t = n[::-1]
    return t
s ="qwewq"
l = reverse(s)
print(l)
if(l == s):
    print(f"This string is palindrome")
else:
    print(f"This string is not palindrome")
