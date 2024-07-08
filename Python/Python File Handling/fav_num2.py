import json
file_name='fav_num.json'
with open(file_name) as f:
    fav_num=json.load(f)
print(f"I know your favorite number! It's {fav_num}")