#!\workspace\python37\python

# Define Variables

nombre = "Andres"
apellido = "Chaparro"

# Print Variables

print(nombre, apellido)

# Create an array

users = ["Jonathan","Chaparro","Jimmy"]

# Examples of printing in an array

print(users[0])

print(users[len(users)-1])

print(users[-1])

users[1] = "Andres"

users.insert(1,"Luis")

users.append("Chon")

# Remove examples

#############remove = users.pop(0)
#############users.remove("user4")

# Function sort

print(sorted(users))

print(users)

# Examples of a loop

for u in users:
    print(u)

for u in range(1, len(users) - 1 ):
    print(users[u])

# Print a slice 

print(users[1:-1])

