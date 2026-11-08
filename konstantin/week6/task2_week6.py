nums = [3, 7, 2, 9, 4, 1, 8]

# I.
nums.append(5)

# II.
nums.remove(9)

# III.
nums = sorted(nums)

#for i in nums:
#    for j in

# IV.
nums = nums[::-1]

for i in range(len(nums) // 2):
    nums[i], nums[-(i + 1)] = nums[-(i + 1)], nums[i]

# V.
nums.insert(2, 6)

# VI.
print("Index of number 4 in list:", nums.index(4))
