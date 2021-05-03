def duplicate_count(name):
    if len(name) > 0:
        name = name.lower()  # convert to lower case
        first_char = name[0]  # get the first char
        match = 0  # number of matches for two or more occurrences
        name = name.replace(first_char, '', 1)  # replace just the 1st instance of the first char
        for x in name:
            if first_char in name:  # if there is an occurrence
                name = name.replace(first_char, '')  # replace all the matches of that char
                match = match + 1  # increment count
            first_char = x  # assign current char
            name = name.replace(first_char, '', 1)  # replace just the 1st occurrence
        return match
    else:
        return 0