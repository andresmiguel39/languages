#!\workspace\python37\python

nombre = "Andres"
apellido = "Chaparro"

print(nombre, apellido)


users = ["Jonathan","Chaparro","Jimmy"]

print(users[0])

print(users[len(users)-1])

print(users[-1])

users[1] = "Andres"

users.insert(1,"Luis")

users.append("Chon")

#remove = users.pop(0)
#users.remove("user4")

print(sorted(users))

print(users)


for u in users:
    print(u)

for u in range(1, len(users) - 1 ):
    print(users[u])

print(users[1:-1])

