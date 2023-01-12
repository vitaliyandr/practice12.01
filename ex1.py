try:
    text = input('text->')
    print(text[::-1])
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
