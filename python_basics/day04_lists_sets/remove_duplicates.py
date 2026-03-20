def remove_duplicates(nums):
    return list(set(nums))


numbers = [1, 2, 2, 3, 4, 4, 5]

print("Original:", numbers)
print("Without duplicates:", remove_duplicates(numbers))