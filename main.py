# Prints line of equal signs 
print ("===============================================")

# Display a greeting to the customer 
print ("Welcome to the Electric Car Customiaztion Club")

print ("Please review the following form !")

# Prints line of equal signs 
print ("================================================")

# Print blank line 
print ()

# Instructions for how to handle multiple choice 
print (f"For multiple choice problems, please enter the letter of the selection you're looking for")

# Display section header 
print ("~ Make & Model ~")

# Display the question
print ("1. What electric vehicle model are you ordering ?")

#Dispaly answer choices 
print ("  a. Ford Mustang Mach-E")
print ("  b. Tesla Model X")
print ("  c. GMC HUMMER EV")
print ("  d. Audi e-tron")

# User inputs car model selection
carmodel = input("Please enter 'a' - 'd':")

# Print blank line 
print ()

# Display the question 
print (f"2. Would you like to upgrade from the standard battery to the supercharged?")

# user selects yes or no
battery = input("Please enter 'yes' or 'no': ")

# Print blank line 
print()

# Display section header 
print ("~ Interior ~")

# Display the question
print ("3. What type of interior would you like in your vehicle?")

# User inputs answer selection
interior = input (f"You may enter the type of material you'd like for your vehicle: ")

# print blank line
print ()

# Display the question
print ("4. Would you like your vehice to come with Apple Carplay ?")

# User selects yes or no
carplay = input ("Please enter 'yes' or 'no': ")

#Print blank line 
print ()

# Display section header
print ("~Exterior~")

# Display the question 
print ("5. Would you like to upgrade to the sports package ?")
sports = input ("Please enter 'yes' or 'no': ")

# print blank line
print ()

# Display the question
print ("6. What color would you like your brake calipers to be ?")
print ("  a.red")
print ("  b.orange")
print ("  c.black")

# User inputs answer selection
brakes = input("Please enter 'a' - 'c': ")

# print blank space
print ()

# print line of equal signs
print ("================================================")

# Display summary text 
print ("~ Summary~ ")

#display carmodel answer
print (f"Model Option: {carmodel}")

# display car battery answer
print (f"Upgrade to supercharged: {battery}")

#display interior option answer
print (f"Interior Material: {interior}")

# display apple carplay answer  
print (f"Apple CarPlay: {carplay}")

# display sports package answer
print (f"Sports package: {sports}")

# display brake caliper answer
print (f"Brake Caliper option: {brakes}")