t = int(input())

users = []
for i in range(t):
    age, name = input().split()
    age = int(age)
    users.append((age, name, i))

users = sorted(users, key = lambda x : (x[0], x[2]))


for user in users:
    print("{} {}".format(user[0], user[1]))