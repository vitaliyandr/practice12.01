try:
    string = input("Enter a string: ")
    char = input("Enter a character to search for: ")
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(f"The character '{char}' appears {count} times in the string.")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
