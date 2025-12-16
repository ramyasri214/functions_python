# 1. Armstrong Number (no string/list)
n = int(input("Enter number: "))
temp = n
count = 0

# count digits
t = n
while t > 0:
    count += 1
    t //= 10

sum_pow = 0
while temp > 0:
    d = temp % 10
    sum_pow += d ** count
    temp //= 10

print("Armstrong" if sum_pow == n else "Not Armstrong")

# 2. Prime Digit Count

n = int(input("Enter number: "))
count = 0

while n > 0:
    d = n % 10
    if d in (2, 3, 5, 7):
        count += 1
    n //= 10

print("Prime digits count:", count)

# 3. Number Pyramid (Arithmetic)

n = int(input("Enter rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 4. Prime Numbers in a Range

start = int(input("Start: "))
end = int(input("End: "))

for n in range(start, end + 1):
    if n > 1:
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)

# 5. GCD and LCM (loops only)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

x, y = a, b
while x != y:
    if x > y:
        x -= y
    else:
        y -= x

gcd = x
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)

# 6. Digit Alternation Check (Even–Odd)
                            
n = int(input("Enter number: "))
prev = n % 10
n //= 10
flag = True

while n > 0:
    curr = n % 10
    if (prev % 2) == (curr % 2):
        flag = False
        break
    prev = curr
    n //= 10

print("Alternating" if flag else "Not Alternating")

# 7. Binary → Decimal (no string/int)

n = int(input("Enter binary: "))
power = 1
decimal = 0

while n > 0:
    bit = n % 10
    decimal += bit * power
    power *= 2
    n //= 10

print("Decimal:", decimal)

# 8. Decimal → Binary (no string)

n = int(input("Enter decimal: "))
binary = 0
place = 1

while n > 0:
    binary += (n % 2) * place
    place *= 10
    n //= 2

print("Binary:", binary)

# 9. Kaprekar Number

n = int(input("Enter number: "))
sq = n * n
temp = sq
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

div = 10 ** (digits // 2)
left = sq // div
right = sq % div

print("Kaprekar" if left + right == n else "Not Kaprekar")

# 10. N-th Prime Number

n = int(input("Enter N: "))
count = 0
num = 2

while True:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1
        if count == n:
            print("Nth Prime:", num)
            break
    num += 1

# 🔀 Advanced Conditionals + Loops
# 11. Custom Pattern

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

# 12. Happy Number

n = int(input("Enter number: "))

while n != 1 and n != 4:
    s = 0
    while n > 0:
        d = n % 10
        s += d * d
        n //= 10
    n = s

print("Happy" if n == 1 else "Not Happy")

# 13. Harshad (Niven) Number

n = int(input("Enter number: "))
temp = n
s = 0

while temp > 0:
    s += temp % 10
    temp //= 10

print("Harshad" if n % s == 0 else "Not Harshad")

# 14. Number Reduction Game (Collatz)

n = int(input("Enter number: "))
steps = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    steps += 1

print("Steps:", steps)

# 15. Sum of digits = Product of digits (1–1000)
                                       
for n in range(1, 1001):
    temp = n
    s = 0
    p = 1
    while temp > 0:
        d = temp % 10
        s += d
        p *= d
        temp //= 10
    if s == p:
        print(n)

# 16. Magic Number

n = int(input("Enter number: "))

while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s

print("Magic Number" if n == 1 else "Not Magic")

# 17. Reverse & Prime Check

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Both Prime" if is_prime(n) and is_prime(rev) else "Not Both Prime")

# 18. Strictly Increasing / Decreasing Digits

n = int(input("Enter number: "))
prev = n % 10
n //= 10
inc = dec = True

while n > 0:
    curr = n % 10
    if curr >= prev:
        inc = False
    if curr <= prev:
        dec = False
    prev = curr
    n //= 10

print("Increasing" if inc else "Decreasing" if dec else "Neither")

# 19. Square Pattern (row-wise)

n = int(input("Enter size: "))
num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()

# 20. Smallest Number > N divisible by 7 and its reverse also divisible by 7

n = int(input("Enter N: "))
num = n + 1

while True:
    temp = num
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    if num % 7 == 0 and rev % 7 == 0:
        print("Answer:", num)
        break
    num += 1
