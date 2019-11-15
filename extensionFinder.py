import magic

if 'ASCII tex' in magic.from_file('hello.txt'):
    print('text')
else:
    print('docs')


