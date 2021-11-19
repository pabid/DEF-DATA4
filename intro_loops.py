
# #FOR loops
# cool_cows=["Winnie the moo", "Moolan", "Milk Shake"]

# for loopvar in cool_cows:
#     print(loopvar)

# for loopvar in cool_cows:
#     print(loopvar.upper())

# cool_cows="Winnie the moo"

# for loopvar in cool_cows:
#     print(cool_cows)


# #FOR  - RANGE generate an iterable of numbers based on specified values.
# for loopvar in  range():
#     print(loopvar)

# #starts from 10,  doesnt include 21 and  increments in 2s
# 
for i in range(10, 21, 2):
    print(i)

##########################################
#WHILE
Score = 500
while Score > 100 or Score < 0:
    Score = int(input("enter a score: "))
    if Score > 100 or Score < 0:
        print("Not a valid score, try again")
if Score >= 85:
    print("Distinction")
elif Score >= 65:
    print("Pass")
else:
    print("Fail")

#######################################

#names of 5 people, and for each person 
#prints their name followed by the text "is awesome!"
count = 0
while count < 5:
    name = str(input("What is your name?"))
    print(f"{name}, is awesome!")
    count += 1


# #by leaon
count = 0
friends = []
while count < 5:
    name = input("enter your name: ")
    friends.append(name)
    count += 1 
for friend in friends:
    print(friend, "is awesome")


#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

#Print numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)

for i in range(1500,2701,7):
    if (i)%5 == 0:
        print(i)


#====================================

#convert temperatures to and from celsius, fahrenhei
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

temptype = str(input("Enter a C or F: "))
temp= int(input("Enter the tempeture you wish to convert: "))


if temptype.upper() == "C":
    print(str(temp) + "°C is " + str(((temp/5) * 9) + 32) + " in Fahrenheit")
else:
    temptype.upper() == "F"
    print(str(temp) + "°F is " + str(((temp -32) * 5)/9 ) + " in Celsius")





    