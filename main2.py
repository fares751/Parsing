with open('user_info2.txt', 'r') as f:
    data = f.read()


def parse_user(user_string):
    # Split one user's text into a list of lines.
    user_list = user_string.split('\n')

    # The first line looks like ">51612315".
    # [1:] skips the first character (>), and int() converts the rest to a number.
    user_id = int(user_list[0][1:])

    # "Name: Sarah Johnson" becomes ["Name", "Sarah Johnson"].
    # [1] selects the name. The 1 in split() means split only once.
    name = user_list[1].split(': ', 1)[1]

    # Extract the age the same way, then convert it to an integer.
    age = int(user_list[2].split(': ', 1)[1])

    # People can have different numbers of favorite foods.
    # Find where Purchase_History starts instead of using a fixed position.
    purchase_history_index = user_list.index('Purchase_History:')

    favorite_foods = []

    # Foods start at index 4 and stop before "Purchase_History:".
    # A slice includes the start index but excludes the end index.
    for food in user_list[4:purchase_history_index]:
        # Remove the tabs or spaces before each food.
        favorite_foods.append(food.strip())

    purchase_history = []

    # + 1 skips the "Purchase_History:" heading.
    # Leaving the end empty means take all remaining lines.
    for purchase in user_list[purchase_history_index + 1:]:
        # Convert each amount to an integer so we can add them later.
        purchase_history.append(int(purchase.strip()))

    user_dict = {
        'id': user_id,
        'name': name,
        'age': age,
        'favorite_foods': favorite_foods,
        'purchase_history': purchase_history
    }
    return user_dict


def print_total_spent(user_dicts):
    for user_dict in user_dicts:
        # sum() adds all the numbers in the purchase_history list.
        total = sum(user_dict['purchase_history'])

        # An f-string inserts the values inside {} into the text.
        print(f"{user_dict['name']}: {total}")


# Remove whitespace at the beginning and end of the file.
# Then split at blank lines: each part contains one user's record.
user_strings = data.strip().split('\n\n')

user_dicts = []
for user_string in user_strings:
    user_dict = parse_user(user_string)
    user_dicts.append(user_dict)

print(user_dicts)
print_total_spent(user_dicts)