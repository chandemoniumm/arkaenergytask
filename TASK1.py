def adult(users):
    return [user['name'] for user in users if user.get('age', 0) > 18]

n=int(input("Enter the number of Users: "))
users=[]
for _ in range(n):
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    users.append({'name':name, 'age' : age})
adults= adult(users)
print("The adults in the list are: ", adults)