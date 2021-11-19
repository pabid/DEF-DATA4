# Program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def grade(homework, assessment, exam):
    
    mark = round(((homework+ assessment+exam)/175) * 100,2)
    return mark

############################################

def score(maxscore, std_score):

    if std_score >  maxscore:  
        return f"Invalid score: score entered greater than {maxscore}"
    elif std_score < 0: return 0
    else: 
        return std_score

name=input("Enter the name of the student: ") 

homewkSCORE= score(25,int(input("enter a homework score: ")))

assessmentSCORE=score(50,int(input("enter a assessment score: "))) 

examSCORE= score(100,int(input("enter a exam score: ")))


###########################################



ict_grade = grade(homewkSCORE,assessmentSCORE,examSCORE) 

if ict_grade > 100:
    print(f"{name}: ICT Grade is {ict_grade}%  Distinction")
elif ict_grade >=60 and ict_grade < 85:
    print(f"{name}: ICT Grade is {ict_grade}%  Pass")
else:
    print(f"{name}: ICT Grade is {ict_grade}%  Fail")



#################################################