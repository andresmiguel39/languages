#!\workspace\python37\python

# Simple form of "for" statement 

for u in "four":
    print(u)

# Create an array

users = ["Jonathan","Chaparro","Jimmy"]

# A "for" in a print function

print([u + " " for u in "four"])

# A "for" in a print function with '*'.join function

print('*'.join([u + " " for u in "four"]))

# an "if" statement examples with "and" and "or"

if users[0] == "Jonathan" and users[2] == "Jimmy":
    print("Jimmy")

if users[0] == "Jonathan" or users[1] == "Jimmy":
    print("Jonathan")

if "Jimmy" in    users:
    print("Jimmy found")

# Python Dictionary

users = {
    "nombre":"Jonathan",
    "años":31,
    "profesion":"ingeniero de sistemas"
}

users1 = {
    "nombre":"Jimmy",
    "años":86,
    "profesion":"Kacorro"
}

# Print a part of a dictionary 

print(users["nombre"])

# create an empty array

todo = [] 

# Adding dictionaries to an array

todo.append(users)
todo.append(users1)

# Printing an array of dictionaries

for y in todo:
    print(y)