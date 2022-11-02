#!/usr/bin/python3
# List methods

"""
>>>>List have another problem.
        a = [1, 2, 3, 4]
        b = a
        b[0] = 100
        print(a)  -> The content in the 'a' has also been changed.
        # Because b is referencing to the a.
        # It applies to the all the mutable object.
>>>> Methods
        Same like functions, but it is called on value.
        Eg: "hello".replace("h", "")
>>>>
>>>>
>>>>
"""
order_info = ["pizza", "cheese", "water", "burger"]

# Print the index of an item in the list, if value not in list, it will throw an exception.
print(order_info.index("pizza"))

# Multiple assignment.
red, green, blue = [255, 122, 45]
yellow, orange, white = 144, 15, 78

# Delete am element from the list.
del order_info[0]

# To sort a list of strings in correct alphabetical order
# We cannot sort a list that contain the integer and strings.
# Sorting will be based on the ASCII-betical order.
# A > B >...Z > a > b > c...z  The sorting order is like this.

# Convert all elements into lower case and then sort.
order_info = order_info.sort(key=str.lower)

# Expanding the elements of a list over multiple lines.
fruits_list = ["Apple",
               "Orange",
               "Grapes",
               "Water Melon"]
print(fruits_list)
