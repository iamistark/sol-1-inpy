def moveZeroes(nums):
    
    i = 0 
    j = 0

    while j < len(nums):
        if nums[j] != 0:
            
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

# Driver
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
