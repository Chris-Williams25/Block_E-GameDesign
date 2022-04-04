#Chris Williams
#Learning Files:
#a) open/create a fule b) write 'w' c) append 'a' d) rad 'r'  e) the last time that you read the file, close it

import pygame,os,datetime,time,random 
date=datetime.datetime.now()
score=123
name='Jessie' 
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y'+'\n')
print(scoreLine)
#open a file and write in it
myFile=open('ClassStuff\sce.txt','w')
#if you have a specical text command thing such as \n or \t, you have to use \\ instead of just \ 
#also, if it is in the same folder, you doing have to include the first part (ClassStuff) becuase it just assumes it us.
myFile.write(scoreLine)
myFile.close()

score=345
name='jay' 
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y'+'\n')
print(scoreLine)

myFile=open('ClassStuff\sce.txt','a')
#if you have a specical text command thing such as \n or \t, you have to use \\ instead of just \ 
#also, if it is in the same folder, you doing have to include the first part (ClassStuff) becuase it just assumes it us.
myFile.write(scoreLine)
myFile.close()

myFile=open('ClassStuff\sce.txt','r')
lines= myFile.readline()
print (lines)
lines= myFile.readline()
print (lines)
myFile.close()