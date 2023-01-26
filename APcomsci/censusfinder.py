import csv


myDictionary ={}

working=True 
while(working):
    name=input("Whats the name: ")
    with open('APcomsci\TX.csv', newline='') as csvfile:
        reader= csv.DictReader(csvfile)      
        for row in reader:
            number=row["NUMBER"]
            names=row["NAME"]
            year=row["YEAR"]


            try:
                # if names == name and year == '2021':
                #     print(myDictionary[names][number]+' this year')
                # if names == name and year == '2020':
                #     print(myDictionary[names][number]+' this year')
                # if names == name and year == '2019':
                #     print(myDictionary[names][number]+' this year')
                # if names == name and year == '2018':
                #     print(myDictionary[names][number]+' this year')
                # if names == name and year == '2017':
                #     print(myDictionary[names][number]+' this year') 

                if names == name and year == '2021':
                    print(names+': '+number+': 2021')
                if names == name and year == '2020':
                    print(names+': '+number+': 2020')
                if names == name and year == '2019':
                    print(names+': '+number+': 2019')
                if names == name and year == '2018':
                    print(names+': '+number+': 2018')
                if names == name and year == '2017':
                    print(names+': '+number+': 2017')


            except:
                print("sorry, we couldn't find anything")
        if not(names == name):
            print('Try Again!')
            working=False 
            working=True


