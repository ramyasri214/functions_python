# task:

#  Take a string print all upper case letters at first and lower case letters at last  without using method

s="ChaiTaNya"
upper_chars=" "
Lower_chars=" "
for char in s:
    if char.isupper():
        upper_chars+=char
    else:
        Lower_chars+=char
        result=upper_chars+Lower_chars
print(result)


# python code no methods:
s = input("Enter string: ")

upper = ""
lower = ""

for ch in s:
    if 'A' <= ch <= 'Z':      # ASCII check
        upper += ch
    elif 'a' <= ch <= 'z':
        lower += ch

print(upper + lower)