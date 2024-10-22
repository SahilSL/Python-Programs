# DSPD Practical No.3 (Third time practical in DSPD)
# Made by Vipul

'''
user_input = input("Enter elements that you want in list: ")  # Getting user input as a list
user_list = user_input.split()                                # Input is in string. Splitting strings of numbers into elements list.
for i in range(len(user_list)):                               # Converting that string list into integer list so that we can perform
    user_list[i] = int(user_list[i])                          #  operations on that list.
array = user_list                                             # we got proper data structure of integer type to execute operation
print("Your array is: ", array)

# Recursion Binary Search
n = int(input("Enter elements that you want to search: "))


def binary_search(array, low, high, n):
    if high >= low:
        mid = (low + high) // 2
        if array[mid] == n:
            return mid
        elif array[mid] > n:
            return binary_search(array, low, mid - 1, n)
        else:
            return binary_search(array, mid + 1, high, n)
    else:
        return -1


r = binary_search(array, 0, len(array) - 1, n)
if r != -1:
    print("Element found at Index.", r)
else:
    print("Element not present.")
'''
# -------------------------------------------------------------------------

# Selection sorting



array = [1, 2, 70, 56, 48, 28]
n = len(array)

for i in range(n):
    minimum = i
    for j in range(i + 1, n):
        if array[minimum] > array[j]:
            minimum = j

    array[i], array[minimum] = array[minimum], array[i]  # swapping the minimum element to very first position

print("Sorted array: ")
sorted_array = []
for i in range(len(array)):
    sorted_array.append(array[i])
print(sorted_array)