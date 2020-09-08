import pytest
import re


def search_by_simple_string_matching(search_term, file_path):
    count = 0
    search_term = re.sub(r'\W+', '',search_term.lower())
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split():
                temp = re.sub(r'\W+', '',word.lower())
                if temp == search_term:
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
    words_dict = dict()
    search_term = re.sub(r'\W+', '',search_term.lower())
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split():
                temp = re.sub(r'\W+', '', word.lower())
                print(f'{temp}')
                if temp in words_dict:
                    words_dict[temp] += 1    
                else:
                    words_dict[temp] = 1

    print(f"{words_dict}")    
    
    if search_term in words_dict:
        return words_dict[search_term]
    else: 
        return 0


def main():
    pass


if __name__ == '__main__':
    main()