import json

def get_stored_username():
    """Get stored username if available."""
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_name

def get_new_username():
    """Prompt for a new username"""
    file_name = 'username.json'
    user_name = input("What's your name? ")
    with open(file_name, 'w') as f:
        json.dump(user_name, f)
    return user_name

def greet_user():
    """Greet the user by name."""
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome back, {user_name}")
    else:
        new_username = get_new_username()
        print(f"We'll remember you when you come back, {new_username}!")

greet_user()