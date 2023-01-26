import csv


myDictionary ={}

personal=input("Whats the name: ")
with open('APcomsci\TX.csv', newline='') as csvfile:
    reader= csv.DictReader(csvfile)      
    for row in reader:
        number=row["NUMBER"]
        names=row["NAME"]
        year=row["YEAR"]
        if not(names in myDictionary):
            myDictionary[names]={}
        if not(year in myDictionary[names]):
            myDictionary[names][year] = int(number)
        else:
            myDictionary[names][year] += int(number)
            # print(myDictionary)

try:
    print(myDictionary[personal]['2017'])
    print(myDictionary[personal]['2018'])
    print(myDictionary[personal]['2019'])
    print(myDictionary[personal]['2020'])
    print(myDictionary[personal]['2021'])

except:
    print('cannot find')






        #     try:
        #         # if names == name and year == '2021':
        #         #     print(myDictionary[names][number]+' this year')
        #         # if names == name and year == '2020':
        #         #     print(myDictionary[names][number]+' this year')
        #         # if names == name and year == '2019':
        #         #     print(myDictionary[names][number]+' this year')
        #         # if names == name and year == '2018':
        #         #     print(myDictionary[names][number]+' this year')
        #         # if names == name and year == '2017':
        #         #     print(myDictionary[names][number]+' this year') 

        #         # if names == name and year == '2021':
        #         #     print(names+': '+number+': 2021')
        #         # if names == name and year == '2020':
        #         #     print(names+': '+number+': 2020')
        #         # if names == name and year == '2019':
        #         #     print(names+': '+number+': 2019')
        #         # if names == name and year == '2018':
        #         #     print(names+': '+number+': 2018')
        #         # if names == name and year == '2017':
        #         #     print(names+': '+number+': 2017')


        #     except:
        #         print("sorry, we couldn't find anything")
        # if not(names == name):
        #     print('Try Again!')
        #     working=False 
        #     working=True


