from sys import argv
# passing the script name and txt file name from the terminal
script, filename = argv

#Opening the txt file using the open command
txt = open(filename)

#Print the txt file name and the contents in the txt file using the read method
print(f"Here's your file {filename}:")
print(txt.read())

# Prompting to input the txt file name using the input function
print("Type the filename again:")
file_again = input("> ")

# Open and printing the txt file using the open function and read method respectively
txt_again = open(file_again)

print(txt_again.read())