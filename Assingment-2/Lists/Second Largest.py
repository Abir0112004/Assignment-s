nums = [10, 5, 20, 8, 15]

largest = nums[0]
second = nums[0]

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n != largest and n > second:
        second = n

print("Second largest: ", second)
