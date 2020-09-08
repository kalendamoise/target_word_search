import os
import sys
from word_search import search_by_simple_string_matching
from word_search import search_by_regular_expression_matching
import pytest

FILE_DIR_NAME = '/sample_files/' 
DIRECTORY = os.getcwd() + FILE_DIR_NAME

def test_search_by_simple_string_matching():
    search_term = 'military'
    file_path = DIRECTORY + 'french_armed_forces.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 4


def test_search_by_simple_string_matching_no_match():
    search_term = 'Kalenda'
    file_path = DIRECTORY + 'french_armed_forces.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 0


def test_search_by_simple_string_matching_hitchhikers():
    search_term = "Hitchhiker's"
    file_path = DIRECTORY + 'hitchhikers.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 5    

    
def test_search_by_simple_string_matching_file_not_found_error():
    search_term = "Hitchhiker's"
    file_path = DIRECTORY + 'made_up_file.txt'
    with pytest.raises(FileNotFoundError):
        search_by_simple_string_matching(search_term, file_path)


def test_search_by_re_matching():
    search_term = 'military'
    file_path = DIRECTORY + 'french_armed_forces.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 4


def test_search_by_re_matching_no_match():
    search_term = 'Kalenda'
    file_path = DIRECTORY + 'french_armed_forces.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 0


def test_search_by_re_matching_hitchhikers():
    search_term = "Hitchhiker's"
    file_path = DIRECTORY + 'hitchhikers.txt'
    assert search_by_regular_expression_matching(search_term, file_path) == 6    

    
def test_search_by_re_matching_file_not_found_error():
    search_term = "Hitchhiker's"
    file_path = DIRECTORY + 'made_up_file.txt'
    with pytest.raises(FileNotFoundError):
        search_by_regular_expression_matching(search_term, file_path)
