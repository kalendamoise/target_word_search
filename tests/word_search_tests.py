from word_search import search_by_simple_string_matching

def test_search_by_simple_string_matching():
    search_term = 'military'
    file_path = 'sample_files/french_armed_forces.txt'
    assert search_by_simple_string_matching(search_term, file_path) == 4