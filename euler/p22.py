def p22():
    with open('H://p022_names.txt', 'r+') as name_file:
        contents = name_file.read()
        contents = contents.replace(',', '\n')
        contents = contents.replace('"', "")
        contents = contents.split('\n')
    contents.sort()

    total = 0
    for name in contents:
        name_sum = 0
        for char in name:
            ascii_value = ord(char) - 64
            name_sum += ascii_value
        total += int(name_sum * (contents.index(name)+1))
    print(total)
