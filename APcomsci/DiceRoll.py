import random, math
#Chris Williams 9/15/2022
twos=0
threes=0
fours=0
fives=0
sixes=0
sevens=0
eights=0
nines=0
tens=0
elevens=0
twelves=0
trialnumber=1
n=input("how many rolls?: ")
for i in range(int(n)):
#make the die
    print("trail number",+trialnumber)
    Die1=random.randint(1,6)
    Die2=random.randint(1,6)
#roll the die 
    # print("\tDie 1 is",+Die1)
    # print("\tDie 2 is",+Die2)
#Add the Die
    Dice=int(Die1)+int(Die2)
    # print("\tThe Dice together are",+Dice)
    #actual ratios
    if Dice == 2:
        twos+=1
    if Dice == 3:
        threes+=1
    if Dice == 4:
        fours+=1
    if Dice == 5:
        fives+=1
    if Dice == 6:
        sixes+=1
    if Dice == 7:
        sevens+=1
    if Dice == 8:
        eights+=1
    if Dice == 9:
        nines+=1
    if Dice == 10:
        tens+=1
    if Dice == 11:
        elevens+=1
    if Dice == 12:
        twelves+=1
#creating the ratios
Aratio2=int(twos)/int(n)
Aratio3=int(threes)/int(n)
Aratio4=int(fours)/int(n)
Aratio5=int(fives)/int(n)
Aratio6=int(sixes)/int(n)
Aratio7=int(sevens)/int(n)
Aratio8=int(eights)/int(n)
Aratio9=int(nines)/int(n)
Aratio10=int(tens)/int(n)
Aratio11=int(elevens)/int(n)
Aratio12=int(twelves)/int(n)

# print("\t\tActual ratios")

# print("1 ",+Aratio2)
# print("2 ",+Aratio3)
# print("3 ",+Aratio4)
# print("4 ",+Aratio5)
# print("5 ",+Aratio6)
# print("6 ",+Aratio7)
# print("7 ",+Aratio8)
# print("8 ",+Aratio9)
# print("9 ",+Aratio10)
# print("10 ",+Aratio11)
# print("11 ",+Aratio12)

#Deviation
Dev2=Aratio2-.03
Dev3=Aratio3-.06
Dev4=Aratio4-.08
Dev5=Aratio5-.11
Dev6=Aratio6-.14
Dev7=Aratio7-.17
Dev8=Aratio8-.14
Dev9=Aratio9-.11
Dev10=Aratio10-.08
Dev11=Aratio11-.08
Dev12=Aratio12-.03

# Dev2=int(Aratio2)-.03
# Dev3=int(Aratio3)-.06
# Dev4=int(Aratio4)-.08
# Dev5=int(Aratio5)-.11
# Dev6=int(Aratio6)-.14
# Dev7=int(Aratio7)-.17
# Dev8=int(Aratio8)-.14
# Dev9=int(Aratio9)-.11
# Dev10=int(Aratio10)-.08
# Dev11=int(Aratio11)-.08
# Dev12=int(Aratio12)-.03

# round(Dev2, 2)
# abs(Dev2)
# round(Dev3, 2)
# abs(Dev3)
# round(Dev4, 2)
# abs(Dev4)
# round(Dev5, 2)
# abs(Dev5)
# round(Dev6, 2)
# abs(Dev6)
# round(Dev7, 2)
# abs(Dev7)
# round(Dev8, 2)
# abs(Dev8)
# round(Dev9, 2)
# abs(Dev9)
# round(Dev10, 2)
# abs(Dev10)
# round(Dev11, 2)
# abs(Dev11)
# round(Dev12, 2)
# abs(Dev12)

# print("\t\tDeviation")

# print("1 ",+abs(round(Dev2,2)))
# print("2 ",+abs(round(Dev3,2)))
# print("3 ",+abs(round(Dev4,2)))
# print("4 ",+abs(round(Dev5,2)))
# print("5 ",+abs(round(Dev6,2)))
# print("6 ",+abs(round(Dev7,2)))
# print("7 ",+abs(round(Dev8,2)))
# print("8 ",+abs(round(Dev9,2)))
# print("9 ",+abs(round(Dev10,2)))
# print("10 ",+abs(round(Dev11,2)))
# print("11 ",+abs(round(Dev12,2)))

print("\n\n\n\n")
print("values  expected ratios  actual ratios  deviation")
# print("2:",+(twos)," .03",+abs(round(Aratio2,2)))
# print("3:",+(threes)," .06"+abs(round(Aratio3,2)))
# print("4:",+(fours)," .08"+abs(round(Aratio4,2)))
# print("5:",+(fives)," .11"+abs(round(Aratio5,2)))
# print("6:",+(sixes)," .14"+abs(round(Aratio6,2)))
# print("7:",+(sevens)," .17"+abs(round(Aratio7,2)))
# print("8:",+(eights)," .14"+abs(round(Aratio8,2)))
# print("9:",+(nines)," .11"+abs(round(Aratio9,2)))
# print("10:",+(tens)," .08"+abs(round(Aratio10,2)))
# print("11:",+(elevens)," .08"+abs(round(Aratio11,2)))
# print("12:",+(twelves)," .03"+abs(round(Aratio12,2))) 

print("2:",+(twos),"    .03             ",+abs(round(Aratio2,2)),"          ",+abs(round(Dev2,2)))
print("3:",+(threes),"    .06             ",+abs(round(Aratio3,2)),"          ",+abs(round(Dev3,2)))
print("4:",+(fours),"    .08             ",+abs(round(Aratio4,2)),"         ",+abs(round(Dev4,2)))
print("5:",+(fives),"    .11             ",+abs(round(Aratio5,2)),"         ",+abs(round(Dev5,2)))
print("6:",+(sixes),"    .14             ",+abs(round(Aratio6,2)),"         ",+abs(round(Dev6,2)))
print("7:",+(sevens),"    .17             ",+abs(round(Aratio7,2)),"         ",+abs(round(Dev7,2)))
print("8:",+(eights),"    .14             ",+abs(round(Aratio8,2)),"         ",+abs(round(Dev8,2)))
print("9:",+(nines),"    .11             ",+abs(round(Aratio9,2)),"         ",+abs(round(Dev9,2)))
print("10:",+(tens),"   .08             ",+abs(round(Aratio10,2)),"         ",+abs(round(Dev10,2)))
print("11:",+(elevens),"   .08             ",+abs(round(Aratio11,2)),"         ",+abs(round(Dev11,2)))
print("12:",+(twelves),"   .03             ",+abs(round(Aratio12,2)),"          ",+abs(round(Dev12,2)))

# print("2:",+(twos)," .03",+(Aratio2),+abs(round(Dev2,2)))
# print("3:",+(threes)," .06"+(Aratio3)+abs(round(Dev3,2)))
# print("4:",+(fours)," .08"+(Aratio4)+abs(round(Dev4,2)))
# print("5:",+(fives)," .11"+(Aratio5)+abs(round(Dev5,2)))
# print("6:",+(sixes)," .14"+(Aratio6)+abs(round(Dev6,2)))
# print("7:",+(sevens)," .17"+(Aratio7)+abs(round(Dev7,2)))
# print("8:",+(eights)," .14"+(Aratio8)+abs(round(Dev8,2)))
# print("9:",+(nines)," .11"+(Aratio9)+abs(round(Dev9,2)))
# print("10:",+(tens)," .08"+(Aratio10)+abs(round(Dev10,2)))
# print("11:",+(elevens)," .08"+(Aratio11)+abs(round(Dev11,2)))
# print("12:",+(twelves)," .03"+(Aratio12)+abs(round(Dev12,2)))

# print("2:",+(twos)," .03",+(Aratio2),+(Dev2))
# print("3:",+(threes)," .06",+(Aratio3),+(Dev3))
# print("4:",+(fours)," .08",+(Aratio4),+(Dev3))
# print("5:",+(fives)," .11",+(Aratio5),+(Dev4))
# print("6:",+(sixes)," .14",+(Aratio6),+(Dev5))
# print("7:",+(sevens)," .17",+(Aratio7),+(Dev6))
# print("8:",+(eights)," .14",+(Aratio8),+(Dev7))
# print("9:",+(nines)," .11",+(Aratio9),+(Dev8))
# print("10:",+(tens)," .08",+(Aratio10),+(Dev9))
# print("11:",+(elevens)," .08",+(Aratio11),+(Dev10))
# print("12:",+(twelves)," .03",+(Aratio12),+(Dev12))


