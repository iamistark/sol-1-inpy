def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    missing = -1

    # Find the duplicate number
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    # Find the missing number
    for num in range(1, n + 1):
        if num not in num_set:
            missing = num

    return [duplicate, missing]

# Driver code
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
