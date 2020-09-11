import re
import timeit
import os
from collections import OrderedDict
import queue


def search_by_simple_string_matching(search_term, file_path):
    """
    simple string matching search

    :param search_term: the word to search for
    :param file_path: the path of the file in which to search
    :return: the number of time the search term was found
    """
    count = 0
    search_term = re.sub(r'\W+', '', search_term.lower())
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split():
                temp = re.sub(r'\W+', '', word.lower())
                if temp == search_term:
                    count += 1

    return count


def search_by_regular_expression_matching(search_term, file_path):
    """
    Regular Expression search

    :param search_term: the word to search for
    :param file_path: the path of the file in which to search
    :return: the number of time the search term was found
    """
    count = 0
    search_val = f"(?=({search_term.lower()}))"
    with open(file_path) as file:
        for line in file:
            # re.finditer(,) return an iterable with stating index of each match.
            # the length of the returned array represent the number of matched word
            count += len([x for x in re.finditer(search_val, line.lower())])
    return count


def build_dict(file_path):
    """
    build a dictionary from the provided file_path

    :param file_path: the path of the file from which to create a dictionary
    :return: a diction of string key and the number of time that string is present in the file value
    """
    words_dict = dict()
    with open(file_path) as file:
        for line in file:
            for word in line.split():
                # remove all non alphanumeric and white spaces
                temp = re.sub(r'\W+', '', word.lower())
                if temp in words_dict:
                    words_dict[temp] += 1    
                else:
                    words_dict[temp] = 1
    return OrderedDict(words_dict)


def search_by_index(search_term, words_dict):
    """
    Search by index matching search

    :param search_term: the word to search for
    :param words_dict: the dictionary containing string keys to search for
    :return: the number of time the search term was found
    """
    search_term = re.sub(r'\W+', '', search_term.lower())
    if search_term in words_dict:  
        return words_dict[search_term]
    return 0


def print_results(search_results, elapse_time):
    """
    Print the results of a given term search

    :param search_results: the list of results for each file
    :param elapse_time: the time it took execute the search
    """
    my_queue = queue.PriorityQueue(len(search_results))
    for result in search_results:
        my_queue.put((result[0] * -1, result[1]))

    print(f'\nSearch results: ')
    while not my_queue.empty():
        val = my_queue.get()
        print(f'\t{val[1]} - {val[0] * -1 } matches')

    print(f'Elapsed time: {elapse_time} ms')
    print("")


def search(search_type, search_term, base_dir, *args):
    """
    execute search for in all files

    :param search_type: the type fo search execute
    :param search_term: term to search for
    :param base_dir: the base directory from which this program is executing
    :param args: text file(s)
    :return a tuple containing the search result and elapse time.
    """
    dictionaries = []
    if search_type == '3':
        for _file in args:
            dictionaries.append(build_dict(os.path.join(base_dir, _file)))

    start_time = timeit.default_timer()
    search_results = []
    for index, _file in enumerate(args):
        if search_type == "1":
            result = search_by_simple_string_matching(search_term, os.path.join(base_dir, _file))
        elif search_type == "2":
            result = search_by_regular_expression_matching(search_term, os.path.join(base_dir, _file))
        else:
            result = search_by_index(search_term, dictionaries[index])

        search_results.append((result, _file))

    stop_time = timeit.default_timer()
    elapse_time = stop_time - start_time

    return search_results, elapse_time


def main():
    base_dir = os.path.join(os.getcwd(), 'sample_files')
    file1 = 'french_armed_forces.txt'
    file2 = 'hitchhikers.txt'
    file3 = 'warp_drive.txt'
    
    print("")
    search_term = input("Enter the search term: ").strip()
    search_method = input("Search Method: 1)String Match 2)Regular Expression 3)Indexed ").strip()
    while search_method not in ('1', '2', '3'):
        print("Enter one of the following values for the options bellow: 1, 2, 3")
        search_method = input("Search Method: 1)String Match 2)Regular Expression 3)Indexed").strip()

    search_results, elapse_time = search(search_method, search_term, base_dir, file1, file2, file3)

    print_results(search_results, elapse_time)


if __name__ == '__main__':
    main()
