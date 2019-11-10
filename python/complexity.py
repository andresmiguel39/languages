#!\workspace\python37\python

for u in "four":
    print(u)

users = ["Jonathan","Chaparro","Jimmy"]

print([u + " " for u in "four"])

print('*'.join([u + " " for u in "four"]))

if users[0] == "Jonathan" and users[2] == "Jimmy":
    print("Jimmy")

if users[0] == "Jonathan" or users[1] == "Jimmy":
    print("Jonathan")

if "Jimmy" in    users:
    print("Jimmy found")

####=========================


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

print(users["nombre"])

todo = [] 

todo.append(users)
todo.append(users1)

for y in todo:
    print(y)