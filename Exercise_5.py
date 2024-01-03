my_name = " Gokula Krishnan Ramachandran" # full name
my_age = 34 # born in 1989
my_height = 178 #cms
my_weight = 94 #Kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = "Black"

print (f"Let's talk about {my_name}.")
print (f"He's {my_height * 0.3937} inches tall.")
print(f"He's {my_weight * 2.2046} pounds heavy.")
print("Actually that is not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")
#print(f"If I add {my_age, my_height} and {my_weight} I get {total}.") # does not work as intended