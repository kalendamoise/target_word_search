import pytest
import re



def search_by_simple_string_matching(search_term, file_path):
    count = 0
    with open(file_path) as file:
        for line in file:
            for word in line.split():
                if word.lower() == search_term.lower():
                    count += 1

    return count


def search_by_regular_expression_matching(search_term, file_path):
    count = 0
    search_val = f"(?=({search_term.lower()}))"
    with open(file_path) as file:
        for line in file:
            # re.finditer(,) return an iterable with stating index of each match. 
            # the length of the returned array represent the number of matched word
            count += len([x for x in re.finditer(search_val, line.lower())])

    return count


def search_by_index(search_term, file_path):
    pass    
