# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()
##################

from os import close


with open("filename.txt", "w") as file:
    for n in range(1,11):
        newline = "This is line" + str(n) + "\n"
        file.write(newline)


################
# myfile = open('README.md')
# chars = myfile.readlines()
# myfile.close()

# chars.insert(2,"I like files\n")
# chars.append("\nCheese is pretty good to eat\n")
# print(chars)
# output = "".join(chars)

# myfile = open('README.md',mode='w')
# myfile.write(output)
# myfile.close()


#Exercise
# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.

with open("teams.txt", "w") as file:
    
    mylist = ["Manchester United", "Liverpool", "Charlon FC","Stevenage FC","Leyton FC"]
    newline1=""  
    for n in mylist:
        newline1 = newline1 + n +  "\n"
        
    file.write(newline1)
    
    



with open("teams.txt", "r") as mfile:
    # reads all the lines into a long list
    nline = mfile.readlines()
    print(nline[1])
    print(nline[-2])


    
