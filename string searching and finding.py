# task:

# 1. Print a specific part of a string without using slicing  

s = input("Enter string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

result = ""

for i in range(start, end):
    result += s[i]

print("Result:", result)

# 2. Print the string to replace "is" with "si" without using replace method

s = input("Enter string: ")
result = ""
i = 0

while i < len(s):
    if i < len(s) - 1 and s[i] == 'i' and s[i+1] == 's':
        result += 's'
        result += 'i'
        i += 2
    else:
        result += s[i]
        i += 1

print("Result:", result)