
#Mark
mark = int(input("Enter your mark: "))

if mark > 85:
    print("Distinction")
elif mark >=60 and mark < 85:
    print("Pass")
else:
    print("Fail")

# #Daniel's
# print("What did the student score?")
# userScore = int(input())
# if type(userScore) == int:
#     if int(userScore) > 85:
#         print("Distinction")
#     elif int(userScore) > 65:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Please enter a valid score.")





#Ex 34
var1 = int(input("Enter a Integer: "))

if (var1%2 == 0):
    print ("it is an even number")
else:
    print ("it is an odd number")


#EX35
human_years =  float(input("Enter a humam age: "))


if (human_years < 0):
    print("Your human hasn't been born yet")
elif human_years <= 2:
    dog_years =  float(10.5)
else:
    dog_years = float(((human_years -2) * 4)  + 10.5)

#Ben Stephenson's The Python Workbook
#Ex36
vowels="aeiou"
letter = str(input("Enter a letter: "))

if len(letter) > 1:
    print("Enter just 1 letter")
elif (letter.lower() == "y"):
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
elif vowels.index(letter.lower()) > 0:
    print(letter + " is a vowel")
else:
    print(letter + " is a consonant")




    


