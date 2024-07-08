import json
file_name = 'fav_num.json'
fav_num = input("What's your favorite number?")
with open(file_name, 'w') as f:
    json.dump(int(fav_num), f)