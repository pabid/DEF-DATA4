
# ## Lottery Ball
# Goal: “Create a lottery ball, or Hat, 
# that takes a variable number of arguments that specify the number of balls of each color that are in the hat. 
#  -- vari 
# Give the object the ability to pick a random number of balls from the hat, 
# which will then be used to compute the probability of picking a certain distribution 
# of balls #  over a large number of experiments”


#Creat a class

import pdb
class Hat:
    def __init__(self,nBalls,nColours):

        self.balls = nBalls
        self.colours = nColours

    def ballstotal(self):
       #the number of balls raised to power the  number of different colours

       return self.balls ** self.colours

    def probability(self):
        #he number of balls  divided by ballstotal

        return ((self.balls/self.ballstotal())*100)


#code to use class

#nput_string = input('Enter colour and number of ball for each colour separated by space eg Black 2: ')

input_string ="Black 5 blue 5 red 5 green 5 yellow 5"
user_list = input_string.split()

i=1 #balls 
x=0 #colour

#list to  list of balls and colours
ball_list=[]
colour_list=[]


# get list  of colours
for x in range(x, len(user_list)- 1, 2):

    colour_list.append(str(user_list[x]))      
    

#get numbers of balls
for i in range(i,len(user_list)-1, 2):
       
    ball_list.append(int(user_list[i]))
    
#variables to data meant for the class 
balls = sum(ball_list)
colours = len(colour_list)

#data  passed to the class Hat
myHat=Hat(balls,colours)
total=myHat.ballstotal()
prob =myHat.probability()


print(f"The Probabilityy of a picking a certain ball out of {total} balls is {prob}%")
