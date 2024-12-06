unit = input("Is this temperature is measured in Celcius of Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp*9)/5 +32,1)
    unit = "Fahrenheit"
    print(f"The temperature in Fahrenheit is : {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5/9,1)
    print(f"The temperature in Celcius is : {temp} C")
else:
    print (f"{unit} is not a valid unit.")