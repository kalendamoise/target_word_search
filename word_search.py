import pytest
import re
import timeit
import os


def search_by_simple_string_matching(search_term, file_path):
    count = 0
    # search_term = re.sub(r'\W+', '',search_term.lower())
    search_term = search_term.lower()
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split():
                # temp = re.sub(r'\W+', '',word.lower())
                temp = word.lower()
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


def build_dict(file_path):
    words_dict = {}
    with open(file_path) as file:
        for line in file:
            for word in line.strip().split():
                #temp = re.sub(r'\W+', '', word.lower())
                temp = word.lower()
                if temp in words_dict:
                    words_dict[temp] += 1    
                else:
                    words_dict[temp] = 1  

    return words_dict

def search_by_index(search_term, words_dict):
    # search_term = re.sub(r'\W+', '',search_term.lower())
    search_term = search_term.lower()    
    if search_term in words_dict:
        return words_dict[search_term]
    
    return 0


def find_using_string_match(search_term, base_dir, file1, file2, file3):
    start_time = timeit.default_timer()

    french_armed_forces =  search_by_simple_string_matching(search_term, os.path.join(base_dir, file1))
    hitchhikers =  search_by_simple_string_matching(search_term, os.path.join(base_dir, file2))
    warp_drive =  search_by_simple_string_matching(search_term, os.path.join(base_dir, file3))
    #dante =  search_by_simple_string_matching(search_term, os.path.join(base_dir, file4))

    stop_time = timeit.default_timer()
    elapse_time = stop_time - start_time
    
    print('String Matching Search results: ')
    print(f'\t{file1} - {french_armed_forces} matches')
    print(f'\t{file2} - {hitchhikers} matches')
    print(f'\t{file3} - {warp_drive} matches')
    #print(f'\t{file4} - {dante} matches')
    print(f'Elapsed time: {elapse_time}')
    print("")


def find_by_regex(search_term, base_dir, file1, file2, file3):
    start_time = timeit.default_timer()

    french_armed_forces =  search_by_regular_expression_matching(search_term, os.path.join(base_dir, file1))
    hitchhikers =  search_by_regular_expression_matching(search_term, os.path.join(base_dir, file2))
    warp_drive =  search_by_regular_expression_matching(search_term, os.path.join(base_dir, file3))
    #dante =  search_by_regular_expression_matching(search_term, os.path.join(base_dir, file4))

    stop_time = timeit.default_timer()
    elapse_time = stop_time - start_time
    
    print('Find by Regex Search results: ')
    print(f'\t{file1} - {french_armed_forces} matches')
    print(f'\t{file2} - {hitchhikers} matches')
    print(f'\t{file3} - {warp_drive} matches')
    #print(f'\t{file4} - {dante} matches')
    print(f'Elapsed time: {elapse_time}')
    print("")


def find_by_index(search_term, base_dir, file1, file2, file3):
    file1_dict =  build_dict(os.path.join(base_dir, file1))
    file2_dict =  build_dict(os.path.join(base_dir, file2))
    file3_dict =  build_dict(os.path.join(base_dir, file3))
    #file4_dict =  build_dict(os.path.join(base_dir, file4))
    
    start_time = timeit.default_timer()

    french_armed_forces =  search_by_index(search_term, file1_dict)
    hitchhikers =  search_by_index(search_term, file2_dict)
    warp_drive =  search_by_index(search_term, file3_dict)
    #dante =  search_by_index(search_term, file4_dict)

    stop_time = timeit.default_timer()
    elapse_time = stop_time - start_time
    
    print('Find By Index Search results : ')
    print(f'\t{file1} - {french_armed_forces} matches')
    print(f'\t{file2} - {hitchhikers} matches')
    print(f'\t{file3} - {warp_drive} matches')
    #print(f'\t{file4} - {dante} matches')
    print(f'Elapsed time: {elapse_time}')
    print("")


def main():
    search_term = input("Enter the search term: ")
    base_dir = os.path.join(os.getcwd(), 'sample_files')
    file1 = 'french_armed_forces.txt'
    file2 = 'hitchhikers.txt'
    file3 = 'warp_drive.txt'
    #file4 = 'dante.txt'

    find_by_index(search_term, base_dir, file1, file2, file3)
    find_using_string_match(search_term, base_dir, file1, file2, file3)
    find_by_regex(search_term, base_dir, file1, file2, file3)





    


    
    
    

if __name__ == '__main__':
    main()