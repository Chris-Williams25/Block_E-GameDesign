# Notes 
# The number assigned to an element in an array is length-1

# A list can be ordered or changed, it allows duplicate members
# A tuple is like a list because its ordered, however, it is unchangeable. It also allows duplicate members.
# A dictionary is unorder changeable

# a list is changable and accepts duplicates

# append() adds elements at the end of a list like if {30, 60, 90} are added to the end of a list
# extend() very similar to append() extend() brings the elements into the list like if ,30,60,90 are added to the end of a list.
# pop() removes the element at a specific position.
import os, random
os.system('cls') 

fruits=["bananas", "grapes", "watermelon", "papaya", "oranges", "tomatoes", "kiwis", "mangos", "apples", "strawberries", "blackberries"]
size=len(fruits) 
print(size)
fruits.append("ranbutan") 
for i in range(size):
    print(fruits[i]) 
    print(fruits[-2]) 
print(fruits[size-1]) #we need to subtract 1 from the size to get the proper element of the list becuase the numbers that are assigned to start at 0
print(fruits.count('blackberries')) 
list2=[3,6,8,9,10]
fruits.append(list2) 
print("append \n",fruits)
fruits.pop(-1) 
fruits.extend(list2) 
print("extend \n",fruits) 
fruits.insert(2, "dragon fruit") 
print(fruits) 
