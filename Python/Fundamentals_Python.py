name = "Afif"
print(type(name))
print(type(name) == str)
print(isinstance(name, str))
age=20
print("Age is",isinstance(age, int))
Age=float(age)
print("Age is float:",isinstance(Age, int))
num="21"
print("AGE = ",num," is str: ",isinstance(num, str))
AGE = int(num)
print("AGE = ",AGE," is int: ",isinstance(AGE, int))

#is Identity operator Returns true while comparing two similar objects 
#in membership operator Tells if a value is present in a list, ssequence etc.
def is_adult(a):
    return True if a>18 else False #Ternary operator
print(is_adult(age))
print("Afif". upper())
print("AfIF".lower())
print("AfiF person".title())
print("afif".islower())
#isalpha() - check if string only contains characters & is not empty
#isalnum() - check if string contains characters or digits 
#isdecimal() - check if string contains only digits
#lower() - lowercase verdsion of a string
#upper() - uppercase version of a string
#startswith() - to check if the string starts with a specific substring
#endswith() - to check if the string ends with a specific substring
#replace() - replaces a part of a string
#split() - separates a string at a specific character separator
#strip() - trim whitespaces from a string
#join() - append new letters to a string
#find() - find position of a substring
print(name[-2])
string = "he is cool"
print(string[:5])
print(string[3:8])
done = False
print(type(done)==bool)
if done:
    print("Yes")
else:
    print("No")
book1_read = True
book2_read = False
read_any_book = any([book1_read, book2_read])
print(read_any_book)
read_all_book = all([book1_read, book2_read])
print(read_all_book)