def count_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        contents = contents.lower()
        words = contents.count('the ')
        print(f"The file {file_name[11:]} has the word 'the' about {words} times.")
file_names = ['text_files\\alice.txt', 'text_files\\siddharta.txt', 'text_files\\little_women.txt', 'text_files\\moby_dick.txt']
for file_name in file_names:
    count_words(file_name)