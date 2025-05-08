#create tuples of 5 colors and print

colors = ("red", "blue", "green", "yellow", "black")
print("The colors are = ",colors)
# Access the 2nd and last elements of a tuple using indexing.
print("2nd element = ",colors[1])
print("Last element = ",colors[-1])
# Find the length of a tuple using len().
length_of_tuple = len(colors)
print("Length of the tuple is = ",length_of_tuple)
# Check if an element exists in a tuple.
if "red" in colors:
    print("Red is present in the tuple.")
else:
    print("Red is not present in the tuple.")

# Convert a list to a tuple using tuple() function.
list_of_numbers = [1, 2, 3, 4, 5]
tuple_of_numbers = tuple(list_of_numbers)
print("Tuple of numbers = ",tuple_of_numbers)
