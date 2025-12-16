
## 🔤 Assume the string


s = "chaitanya"
# Indexes
#  0 1 2 3 4 5 6 7 8
#  c h a i t a n y a
# -9-8-7-6-5-4-3-2-1


## ✅ 1. Print the full string using slicing


print(s[:])


# **Output:**
# 
# chaitanya

## ✅ 2. Print first 5 characters


print(s[:5])


# **Output:**

# chaita

## ✅ 3. Print characters from index 2 to 6


print(s[2:7])


# **Output:**

# ```
# aitan
# `

## ✅ 4. Print string from index 3 till end

print(s[3:])

# **Output:**

# ```
# itanya


## ✅ 5. Print last 4 characters (negative indexing)

print(s[-4:])

# **Output:**

# ```
# nya

## ✅ 6. Print string without first and last character


print(s[1:-1])


# **Output:**


# haitany


## ✅ 7. Print characters at even indexes


print(s[::2])

# **Output:**


# caitna


## ✅ 8. Print characters at odd indexes


print(s[1::2])


# **Output:**

# ```
# hitya

## ✅ 9. Reverse the string using slicing

print(s[::-1])


# **Output:**


# aynatiahc


## ✅ 10. Reverse string except first character


print(s[:0:-1])
# **Output:**


# aynatiah

## ✅ 11. Print string from -6 to -2 index


print(s[-6:-2])

# **Output:**


# tany


## ✅ 12. Print alternate characters from reverse


print(s[::-2])

# **Output:**


# ynia


## ✅ 13. Remove first 3 characters


print(s[3:])

# **Output:**


# itanya


## ✅ 14. Print string except last 3 characters

print(s[:-3])


# **Output:**

# ```
# chaitan




## ✅ 15. Print middle part (`aitan`)


print(s[2:7])


# **Output:**


# aitan




