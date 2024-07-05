file_name = 'text_files\guest.txt'
with open(file_name,'a') as file_object:
    user_name = input("What's your name?\n")
    file_object.write(user_name+"\n")