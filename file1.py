print("Hello world")

print ("Hello World 1") 
print("Hello World 2")
print("Hello World 3")
print("Hello World 4")


Name_in = input("Please enter your name: ")
if Name_in == "":
    print("You did not enter a name")
else:
    print("Hello", Name_in)
#like 1



Input_number_1 = int(input("Please enter a number: "))
Input_number_2 = int(input("Please enter another number: "))

Mathimatical_function = input("Would you like to add, subtract, devide or multiply: ")
Mathimatical_function = Mathimatical_function.lower()

if Mathimatical_function == "add":
    print(Input_number_1 + Input_number_2)

elif (Mathimatical_function) == "subtract":
    print(Input_number_1 - Input_number_2)
    
elif Mathimatical_function == "divide":
    print(Input_number_1 / Input_number_2)
    
elif Mathimatical_function == "multiply":
    print(Input_number_1 * Input_number_2)
else:
    print(Input_number_1 % Input_number_2)
