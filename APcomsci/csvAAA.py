import csv
from tempfile import TemporaryFile

myDictionary={}
n=input("whats the name? ")
# name="NAME"



# years="YEAR"
numbers="NUMBER"
with open('APcomsci\TX.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)
    for row in reader:
        name = row["NAME"]
        year =row["YEAR"]

        if not(name in myDictionary):
            myDictionary[name]={}
        if not(year in myDictionary[name]):
            myDictionary[name][year] = int(row["NUMBER"])
        else:
            myDictionary[name][year] += int(row["NUMBER"])

# try:
#     personal= data[myname]
# except:
#     print("")

# def printName(myname):

# for n in myDictionary:
#     if not(name in myDictionary):
#         print("It's not there, create it") 
#         myDictionary[name]={}
#     print(myDictionary)

#     if not(years in myDictionary[name]):
#         print("it's not there, create it")
#         myDictionary[years]={}
#     print(myDictionary)



    # else:
    #     myDictionary[name][years] = myDictionary[name][years] + str(("NUMBER"))
try:
    print("Printing Values from keys") 
    print(myDictionary[name])
    print(myDictionary[name]["2021"])
    print(myDictionary[name]["2020"])
    print(myDictionary[name]["2019"])
    print(myDictionary[name]["2018"])
    print(myDictionary[name]["2017"])
except:
    print("Can't find a key")