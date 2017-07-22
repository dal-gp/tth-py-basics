# make a list to hold onto our items
# print out instructions on how to use the app
# ask for a new items to our list
# be able to quit
# print out the list


# make a list
shopping_list = []

# print instruction
print("What should we pick up at the store?")
print("""
Enter 'DONE' to stop adding items.
""")

while True:
    # ask for new item
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # add the new item to our shopping list
    shopping_list.append(new_item)

# print out the list
print("Here is your list: ")
for item in shopping_list:
    print(item)
