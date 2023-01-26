import os
print("Library books")
booklist=[]
numbooks=input("how many books to add: ")

for i in range(int(numbooks)):
    books=input('name of book: ')
    booklist.append(books)
print(booklist)
print('there are',+int(numbooks),' books')








