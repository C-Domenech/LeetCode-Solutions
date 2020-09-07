# v1 - It works, but Time Limit Exceeded
# def findDuplicates(nums):
#     duplicates = []
#     for i in range(len(nums)):
#         x = i + 1
#         for j in range(x, len(nums)):
#             if nums[i] == nums[j] and nums[i] not in duplicates:
#                 from bisect import insort
#                 insort(duplicates, nums[i])
#     return duplicates

# v2 - It works fine
def findDuplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            duplicates.append(index + 1)
        nums[index] *= -1
    return duplicates




nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result)
