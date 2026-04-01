def generate_subsets(nums, index=0, current=[]):
    if index == len(nums):
        print(current)
        return

    # Include element
    generate_subsets(nums, index + 1, current + [nums[index]])

    # Exclude element
    generate_subsets(nums, index + 1, current)


nums = [1, 2, 3]
generate_subsets(nums)