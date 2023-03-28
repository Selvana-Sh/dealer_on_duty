# Display all duplicate items from a list.

def find_duplicates(_list):
    seen = set()
    duplicates = set()

    for item in _list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print("Original list was: ", sample_list)
print("Duplicate items are: ", find_duplicates(sample_list))