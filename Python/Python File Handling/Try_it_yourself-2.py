file_name='text_files\learning_python.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'C'))