#Small script that determines how much water you still have left to drink today.

#Determines size of water cup
cup_size = int(raw_input("What cup size did you use today in onces? "))

#Determines how many cups of water you've had so far
amount = int(raw_input("How many cups did you have? "))

#Input your current weight
weight = int(raw_input("How much do you weigh? "))

#Calculates how much water you still need to drink for the day
water_intake = cup_size * amount
need = (weight / 2) - water_intake

#Prints values based on user input
print "So you had %r onces of water, you still need %r onces for today" % (water_intake, need)

