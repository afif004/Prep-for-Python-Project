import json

def get_fav_num():
    file_name = 'fav_num_rem.json'
    fav_num = input("What's your favorite number?")
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
    return fav_num

def print_fav_num():
    file_name = 'fav_num_rem.json'
    try:
        with open(file_name) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num

fav_num = print_fav_num()
if fav_num:
    print(f"I know your favorite number! It's {fav_num}!")
else:
    get_fav_num()