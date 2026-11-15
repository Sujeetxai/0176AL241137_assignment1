numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

numbers = (last, *middle, first)

print("Original Tuple: (10, 20, 30, 40, 50)")
print("After Swapping:", numbers)
