try:  
    original_string = input("Enter the original string: ")
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    modified_string = original_string.replace(word_to_replace, replacement_word)
    print("Modified string: " + modified_string)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')