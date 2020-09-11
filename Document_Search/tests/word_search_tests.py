import os
from Document_Search.word_search import search_by_simple_string_matching
from Document_Search.word_search import search_by_regular_expression_matching
from Document_Search.word_search import search_by_index
from Document_Search.word_search import build_dict
from Document_Search.word_search import search
import random
import pytest


def test_search_by_simple_string_matching():
    search_term = 'military'
    file_path = 'test_files/french_armed_forces.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 4


def test_search_by_simple_string_matching_no_match():
    search_term = 'Kalenda'
    file_path = 'test_files/french_armed_forces.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 0


def test_search_by_simple_string_matching_hitchhikers():
    search_term = "Hitchhiker's"
    file_path = 'test_files/hitchhikers.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 6    

    
def test_search_by_simple_string_matching_file_not_found_error():
    search_term = "Hitchhiker's"
    file_path = 'test_files/made_up_file.txt'
    with pytest.raises(FileNotFoundError):
        search_by_simple_string_matching(search_term, file_path)


def test_search_by_re_matching():
    search_term = 'military'
    file_path = 'test_files/french_armed_forces.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 4


def test_search_by_re_matching_no_match():
    search_term = 'Kalenda'
    file_path = 'test_files/french_armed_forces.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 0


def test_search_by_re_matching_hitchhikers():
    search_term = "Hitchhiker's"
    file_path = 'test_files/hitchhikers.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 6    

    
def test_search_by_re_matching_file_not_found_error():
    search_term = "Hitchhiker's"
    file_path = 'test_files/made_up_file.txt'
    with pytest.raises(FileNotFoundError):
        search_by_regular_expression_matching(search_term, file_path)


def test_search_by_index_matching():
    search_term = 'military'
    file_path = 'test_files/french_armed_forces.txt'
    my_dict = build_dict(file_path)
    assert search_by_index(search_term, my_dict) == 4


def test_search_by_index_no_match():
    search_term = 'Kalenda'
    file_path = 'test_files/french_armed_forces.txt'
    my_dict = build_dict(file_path)
    assert search_by_index(search_term, my_dict) == 0


def test_search_by_index_hitchhikers():
    search_term = "Hitchhiker's"
    file_path = 'test_files/hitchhikers.txt'
    my_dict = build_dict(file_path)
    assert search_by_index(search_term, my_dict) == 6


def test_search_string_match():
    search_term = "the"
    file1 = 'test_files/hitchhikers.txt'
    file2 = 'test_files/french_armed_forces.txt'
    file3 = 'test_files/warp_drive.txt'
    search_type = '1'
    search_results, elapse_time = search(search_type, search_term, "./", file1, file2, file3)
    print(search_results)
    print(elapse_time)
    assert search_results[0][0] == 29
    assert search_results[1][0] == 64
    assert search_results[2][0] == 6

def test_search_regex_match():
    search_term = "the"
    file1 = 'test_files/hitchhikers.txt'
    file2 = 'test_files/french_armed_forces.txt'
    file3 = 'test_files/warp_drive.txt'
    search_type = '2'
    search_results, elapse_time = search(search_type, search_term, "./", file1, file2, file3)
    print(search_results)
    print(elapse_time)
    assert search_results[0][0] == 33
    assert search_results[1][0] == 66
    assert search_results[2][0] == 9


def test_search_index_match():
    search_term = "the"
    file1 = 'test_files/hitchhikers.txt'
    file2 = 'test_files/french_armed_forces.txt'
    file3 = 'test_files/warp_drive.txt'
    search_type = '3'
    search_results, elapse_time = search(search_type, search_term, "./", file1, file2, file3)
    print(search_results)
    print(elapse_time)
    assert search_results[0][0] == 29
    assert search_results[1][0] == 64
    assert search_results[2][0] == 6
