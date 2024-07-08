def read_display_file(file_name):
    try:
        with open(file_name) as f:
            contents=f.read()
    except FileNotFoundError:
        #print(f"The file {file_name[11:]} was not found.")
        pass
    else:
        print(contents.rstrip())
file_names=['text_files\dogs.txt', 'text_files\cats.txt']
for file_name in file_names:
    read_display_file(file_name)