
import random
#Generates random number within a range
print (random.random())
decider = random.randrange(2)
if decider == 0:
    print ("Heads")
else:
    print ("Tails")
print(decider)

#Die Roll Program
print("You rolled a " + str(random.randrange(1,7)))

#Create Lottery Winners from a list of names or numbers)
lotteryWinners=random.sample(range(100), 5)
print (lotteryWinners)

#Create random activity choices for the day
funActivities =["go for hike", "go for swim", "do puzzle", "go on chocolate tour", "go skiing", "watch 3 bodies", "go for a bike ride", "call family", "do laundry", "build program", "bake goodies", "go shopping"]
print(random.choices(funActivities))

