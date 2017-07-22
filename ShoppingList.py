# v1
# make a list to hold onto our items
# print out instructions on how to use the app
# ask for a new items to our list
# be able to quit
# print out the list

# TODO
# have a HELP command
# have a SHOW command
# clean code up in general


def show_help():
    # print out instruction
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def show_list():
    # print out the list
    print("Here is your list: ")
    for item in shopping_list:
        print(item)


# make a list
shopping_list = []

show_help()

while True:
    # ask for new item
    new_item = input("> ")

    # be able to quit the app
    if new_item.upper() == 'DONE':
        break
    if new_item.upper() == 'HELP':
        show_help()
        continue
    if new_item.upper() == 'SHOW':
        show_list()
        continue

    # add the new item to our shopping list
    shopping_list.append(new_item)

show_list()
