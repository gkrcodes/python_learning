def print_two(*argvs):
    arg1, arg2 = argvs
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again (arg1, arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_one(arg1):
    print(f"arg1 : {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Gokul", "Pritha")
print_two_again("Gokula", "Pritha")
print_one("Gokul")
print_none()