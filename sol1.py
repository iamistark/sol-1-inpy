def twoSum(nums, target):
    # Create a dictionary to store the complement of each number
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_dict:
            # If the complement exists in the dictionary, return its index and the current index
            return [complement_dict[complement], i]
        else:
            # Store the current number and its index as a potential complement for future numbers
            complement_dict[num] = i

    # If no solution is found, return an empty list
    return []

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)
