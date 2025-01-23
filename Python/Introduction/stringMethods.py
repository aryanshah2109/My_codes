a = "Aryan"
print(len(a))
print(a.upper())    # this doesn't alter the original string but creates a new string
                    # thus strings are immuatable
print(a.lower())

b = "    Hello   Ara   "
print(b.strip())        # removes white spaces before and after string

c = "!!!!!Jai ho baka!!!!!!!"

print(c.rstrip("!"))    # removes trailling character

print(c.replace("baka", "Johnny"))  # replaces first entered string with second string

d = "hey Aryan i am Jay"
print(d.split())    # converts all the substrings before and after a white space into a list

print(d.capitalize())  
# converts first character into uppercase and rest all into lower case

print(d.center(50)) # centers the string

print(d.count("a"))   # returns count of occurance of given character

print(d.endswith("i"))
print(d.endswith("y")) 
# returns true if character in () is same as last character of string else returns false

e = "He's name is Aryan. He is a good man and is in college"
print(e.find("is"))
#returns index of first occurance of string written in (). if not found, returns -1

#print(e.index("ishhh"))
#same as find() but if not found, gives error

print(e.isalnum())
# returns true if string has only alpha-numerical values
# returns false if any other character other than A-Z, a-z and 0-9 is found. 
# even whites spaces not allowed 

f = "hello"
print(f.isalpha())
# returns true if string has only alphabetical values
# returns false if any other character other than A-Z, a-z is found. 
# even whites spaces not allowed 

print(f.islower())  # true is string is in lower case

print(f.isprintable()) # true is contains only printable characters
# eg of non printable character is '\n'

g = "       "
print(g.isspace())
# returns true if string contains only white spaces

# used to check if a substring is present in given string 
if "Ar" in "Aryan":
    print("Yes")
else:
    print("No")