file_name = 'text_files\learning_python.txt'
with open(file_name) as file_object:
    #contents = file_object.read()
    #for line in file_object:
        #print(line)
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())       
#print("Full file at once:\n"+contents)