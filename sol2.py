def removeElement(nums, val):
    # Initialize two pointers
    i = 0  
    j = 0  

    while j < len(nums):
        if nums[j] != val:
            
            nums[i] = nums[j]
            i += 1
        j += 1

    
    return i

#driver code
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("Count:", k)
print("Modified nums:", nums[:k])
