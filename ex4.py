try: 
    string = input("Enter a string: ")
    word = input("Enter a word to search for: ")
    
    count = string.count(word)
    
    print(f"The word '{word}' appears {count} times in the string.")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
