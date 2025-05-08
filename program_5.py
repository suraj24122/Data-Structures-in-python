# 1. Create a dictionary with 3 key-value pairs
person = {
    "name": "Suraj",
    "age": 20,
    "city": "Hyderabad"
}

# 2. Access and print the value of a specific key
print("Name:", person["name"])  # Accessing the 'name' key

# 3. Add a new key-value pair to the dictionary
person["profession"] = "Student"
print("After adding profession:", person)

# 4. Update the value of an existing key
person["age"] = 21
print("After updating age:", person)

# 5. Delete a key from the dictionary using del
del person["city"]
print("After deleting city using del:", person)

# 5 (continued). Delete a key using pop()
removed_value = person.pop("profession")
print("After using pop to remove profession:", person)
print("Removed value:", removed_value)
