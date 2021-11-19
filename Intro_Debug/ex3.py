#import pdb

#A function to find the factorial of a number using tail recursion
def tail_recursion(factorial, result =1): 
    #pdb.set_trace()
    if factorial == 1:
        return result
    else:
        temp_result = factorial * result
        return tail_recursion((factorial), temp_result)


factorial = int((input("Enter a number:")))
result=10

print(tail_recursion(factorial,result))