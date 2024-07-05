file_name='text_files\guest_book.txt'

with open(file_name, 'a') as file_object:
    while 1:
        user_name = input("What's your name?\n")
        if user_name!="":
            break
    file_object.write(user_name+"\n")