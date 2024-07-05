file_name='text_files\poll.txt'

with open(file_name, 'a') as file_object:
    while 1:
        response = input("Why do you like programming?\n")
        file_object.write(response+"\n")
        if response!="":
            break