pal = [1,2,2,1]

pal_copy = pal.copy()
pal_copy.reverse()

if pal == pal_copy:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")