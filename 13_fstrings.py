import os
os.system('cls')

name = "Piyush"
country = "india"
# Old method to print by formating function
letter = "Hi my name is {0} and I am from {1}"
print(letter.format(name,country))

# new modern method - fstring
print(f"Hi my name is {name} and I am from {country}")


sample = "for only {price:.2f} dollors"
print(sample.format(price = 49.0687))

price_2 = 49.0687
print(f"for only {price_2:.2f} dollors")
