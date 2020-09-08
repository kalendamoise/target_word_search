import pytest





def search_by_simple_string_matching(search_term, file_path):
    count = 0
    with open(file_path) as file:
        for line in file:
            words = line.split(' ')
            for word in words:
                if word == search_term:
                    count += 1

    return count
