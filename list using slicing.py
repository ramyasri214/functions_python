# task:


# 1. Take the list, take the sub list from the list and replace that sublist with sum of the sublist
# 
# using slicing
# 
lst = [10, 20, 30, 40, 50]
start = 1
end = 4

sub_sum = sum(lst[start:end])
lst[start:end] = [sub_sum]

print(lst) 

# withou slicing:
lst = [10, 20, 30, 40, 50]
start = 1
end = 4

sub_sum = 0
for i in range(start, end):
    sub_sum += lst[i]

lst[start:end] = [sub_sum]
print(lst)

# 2. Find the second largest values in a list
# without sorting   

lst = [12, 35, 1, 10, 34, 1]

largest = second = -1

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)  

# with sorting  

lst = [12, 35, 1, 10, 34, 1]

lst = list(set(lst))   # remove duplicates
lst.sort()

print("Second largest:", lst[-2])