import os
#Chris E Williams
#1/14/2021
#Today we will declare variables, print variables, print type of data, learn some operators.
# (#) This symbol is for comments, the computer will ignore these lines if they have the (#)


#This is a program to find the average of 3 tests.

#Declare and assign values
#before I start my code, I want to clear my Terminal, I can do this by (os.sys('clear')
os.system('cls')
test1=89
test2=62.5673
test3=82
Flag=False 

#to display things on the screen, we use the function print.

print(type(test1), type(test2), type(Flag))

#declare sum to add tests symbol for addition is +
Sum = test1 + test2+ test3
# print(Sum)

#for the average, we will use division
Average = Sum/3
# print(Average)
# if you use ctrl + forward + / (as in forward slash) every thing you highlight will become a comment. In order to change it back, you simply do it again to the comment you want to change back.  
#I want to print the average of three tests is (print number)
#any time you want to type letters, you have to use quotation marks.

print("The Average of 3 test is", Average)

print("Test1 =", test1, end=": ")
print("Test2 =", test2, end=": ")
print("Test3 =", test3)