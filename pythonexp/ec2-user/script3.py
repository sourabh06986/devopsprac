#!/usr/bin/python
users = ["user1","user2","user3"]
print (users[0])
#Accessing last element
print (users[len(users)-1])
print (users[-1])
print (users[-2])
users.append("peter")
print users
print users[-1] + " " + users[-2]
#insert element at specific index
users.insert(1,"marry")
users.remove("user1")
print users
