def find_max_min(nums):
    if not nums:
        return None

    max_val = nums[0]
    min_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


numbers = [10, 5, 20, 8, 3]
max_val, min_val = find_max_min(numbers)

print("Max:", max_val)
print("Min:", min_val)