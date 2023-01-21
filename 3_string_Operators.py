import os
os.system('cls')
 

name="!Piyush! !Jasbir! !Piyush!"
password = "AbC123"
blog = 'hi mY namE is : Piyush.'
capitalblog = blog.capitalize()
print("Normal string :",name)
print("Length of string :",len(name)) # find the length of string
print("String in upper case :",name.upper()) # create a string copy & convert to uppercase
print("String in lower case :",name.lower()) # create a string copy & convert to lowercase
print("String without trailling chracters :",name.rstrip("!")) # Remove any trailling chracters from ending
print("Replacing :",name.replace("Piyush","Revanshu")) # that's how replacing works
print("list :",name.split(" ")) # convert the string into list
# captialize function converts the string first letter in uppercase and rest into lowecase
print(capitalblog) # OR #print(blog.capitalize())
print(capitalblog.center(60)) # center the string will move 30 spaces forward and 30 backward
print("Counter Piyush: ",name.count("Piyush")) # Count the given word in string
print("Checking if srting end with '!': ",name.endswith("!")) # Give output in Booleon
print("Checking if Specific part of string end with '!': ",name.endswith("!",0,8)) # Give output in Booleon
print("starting index of 'Jasbir' in sring: ",name.find("Jasbir")) # Give the index of given word in string
print("starting index of 'Jasbir' in sring: ",name.index("Jasbir")) # Give the index of given word in string
# index and find fn() are very similar, differnce is that in find() if we don't get the word it returns -1
# And in the case of index() it will give an error
print("checking from A-Z, a-z & 0-9: ",password.isalnum()) # It check from A-Z, a-z & 0-9 If yes True. If not will return False.
print("check from A-Z and a-z: ",password.isalpha()) # It check from A-Z and a-z.  If yes True. If not will return False.
print("Check if all the char are lower: ",password.islower()) # Check if all the char are lower if not retutn False
print("Check if all the char are Printable: ",password.isprintable()) # Check if all the char are Printable if not retutn False for Ex: if written'\n'
print("checking space in string: ",name.isspace()) # checking only white space in string if not return False
print("Check if all word in string is uppercase: ",blog.istitle()) # check if all word are in uppercase if not return False
print("Checking if it start with 'Hi': ",capitalblog.startswith("Hi")) # Same as endswith
print("Swap the Cases: ",capitalblog.swapcase()) #Convert upper to lower and vice-versa
print("Converting tittle: ",capitalblog.title()) #convert first word into uppercase of every word in string 
