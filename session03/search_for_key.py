items = ["aaa", 111, (4, 5), 2.01] # A set of objects
tests = [(4, 5), 3.14] # Keys to search for

for key in tests: # For all keys
    for item in items: # For all items
        if item == key: # Check for match
            print(key, "was found")
            break
    else:
        print(key, "not found!")

for key in tests: # For all keys
    if key in items: # Let Python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")
