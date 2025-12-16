# Solve the given programs

# chaitanya-> input  

s = "chaitanya"
result = ""

for i in range(1, len(s)):
    if i % 2 == 0:
        result += s[i]

print(result)

# o/p -> aiaa

# concat even positions in string chaitanya  

s = input("Enter string: ")
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print("Even position characters:", result)

# # take two indexes and concat that part of indexes   


# # ex-> 1,4 -> chaitanya -> hai 
# 4  means -> 3

s = "chaitanya"
start = 1
end = 4   # 4 means up to index 3

result = ""

for i in range(start, end):
    result += s[i]

print(result)