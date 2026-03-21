def frequency_counter(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


numbers = [1, 2, 2, 3, 3, 3, 4]

print("Frequency:", frequency_counter(numbers))