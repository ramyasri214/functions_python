# Questions Involving Loops
# 1. Sum of all even numbers between 1 and 100

sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)

# 2. First 10 powers of 2

for i in range(10):
    print(2 ** i)

# 3. Factorial of a number

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 4. Reverse a number

n = int(input("Enter a number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed number:", rev)

# 5. Count number of digits

n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)

# 6. Numbers divisible by both 3 and 5 (1–100)
                                      
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 7. Multiply without using *

a = int(input("Enter a: "))
b = int(input("Enter b: "))
result = 0
for i in range(b):
    result += a
print("Result:", result)

# 8. Sum of digits

n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Sum of digits:", sum_digits)

# 9. Palindrome check (number)

n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# 10. Highest digit in a number


n = int(input("Enter a number: "))
max_digit = 0

while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10

print("Highest digit:", max_digit)

# Questions Involving Conditionals
# 11. Positive, Negative or Zero

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 12. Divisible by 2, 3, both or neither

n = int(input("Enter a number: "))

if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")

# 13. Check three-digit number

n = int(input("Enter a number: "))
if 100 <= abs(n) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 14. Prime number check

n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print("Prime number" if is_prime else "Not a prime number")

# 15. Largest of three numbers


a = int(input("Enter a: "))

b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 16. Leap year check

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 17. Even and greater than 50


n = int(input("Enter a number: "))

if n % 2 == 0 and n > 50:
    print("Even and greater than 50")
else:
    print("Condition not satisfied")


# 18. Number classification


n = int(input("Enter a number: "))

if n < 0:
    print("Negative")
elif 0 <= n <= 9:
    print("Single Digit")
elif 10 <= n <= 99:
    print("Two Digits")
else:
    print("Three or More Digits")



# 19. Square greater than 1000

n = int(input("Enter a number: "))
square = n * n

if square > 1000:
    print("Square:", square)
else:
    print("Square is not greater than 1000")


# 20. Check if one number is a factor of another

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % b == 0:
    print(b, "is a factor of", a)
elif b % a == 0:
    print(a, "is a factor of", b)
else:
    print("Neither is a factor of the other")
