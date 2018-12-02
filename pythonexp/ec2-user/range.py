#!/usr/bin/python
users = ["user1","user2","user3"]
print (users[0])
#Accessing last element
print (users[len(users)-1])
print (users[-1])
print (users[-2])
users.append("peter")
#insert element at specific index
users.insert(1,"marry")
users.remove("user1")
print users
#for loop
for i in range(1,10):
 print (i)
#---
 for i in range(0, len(users)):
  print(users[i])
