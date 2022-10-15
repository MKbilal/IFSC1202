str = input("Enter Values Separated by Spaces: ")
nums = (list(str.split(" ")))
nums = [int(nums[x]) for x in range(len(nums))]
n = len(nums)
min_index = 0
max_index = 0
for x in range(n):
    if nums[x]<nums[min_index]:
        min_index = x
    if nums[x]>nums[max_index]:
        max_index = x

print("Swapped Minimum and Maximum: ", end = " ")
for i in range(n):
    print(nums[i], end = " ")