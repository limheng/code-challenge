# Given an array of size n with range of numbers from 1 to n+1.
# The array doesn’t contain any duplicate, one number is missing, find the missing number.

nums = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16] #missing 13

for index, num in enumerate(nums):
    if index +1 != num:
        print(index + 1)
        break
