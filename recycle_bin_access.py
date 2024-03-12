import winshell

# Get a list of all the files in recycle bin
recycle_bin_items = list(winshell.recycle_bin())

# Iterate over each item and print out its properties
for index, item in enumerate(recycle_bin_items):
    print(f'Item {index + 1}: {item.original_filename()}')

# Delete every item in recycle bin
for recycle_bin_item in recycle_bin_items:
    recycle_bin_item.empty(confirm=True, show_progress=True, sound=True)


# Access and delete a specific item from recycle bin
selected_item = recycle_bin_items[0]
# Undelete the selected item
winshell.undelete(selected_item.original_filename())

# Read content of selected item
with open('r', selected_item.original_filename()) as selected_file:
    content = selected_file.read()
    print(f'Selected file content:\n{content}')

# Delete selected file permanently (optional)
winshell.delete_file(selected_item.original_filename())
        
