my_list = [1, 2, 3, 4, 5]

k = int(input("Enter rotation positions: "))
direction = input("Enter direction (left/right): ")

k = k % len(my_list)

if direction.lower() == "left":
    my_list = my_list[k:] + my_list[:k]
elif direction.lower() == "right":
    my_list = my_list[-k:] + my_list[:-k]

print("Rotated List:", my_list)
