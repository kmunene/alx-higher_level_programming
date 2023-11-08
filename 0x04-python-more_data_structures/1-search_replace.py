#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [str(i) for i in my_list]
    search = str(search)
    replace = str(replace)
    li = []
    for a in range(len(new)):
        for i in new:
            if new[a] == search:
                new[a] = replace
    new_list = [int(i) for i in new]
    return new_list
