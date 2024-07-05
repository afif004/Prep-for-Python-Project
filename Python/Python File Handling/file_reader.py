file_name = 'text_files\pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string=''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in first million digits of pi")
else:
    print("Your birthday does not appear in first million digits of pi")    