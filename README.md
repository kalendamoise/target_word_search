# Document Search

This searches a set of documents for the given term or phrase (single token), and return results in order of relevance. 
Relevancy. Based on the number of times the exact term or phrase appears in the document.
 
It has three methods for searching the documents: 
*	Simple string matching
*	Text search using regular expressions
*	Preprocess the content and then search the index

It prompts the user to enter a search term and search method, execute the search, and return results as follow:
```text
Enter the search term: warp
Search Method: 1)String Match 2)Regular Expression 3)Indexed 1

Search results: 
        warp_drive.txt - 6 matches
        french_armed_forces.txt - 0 matches
        hitchhikers.txt - 0 matches
Elapsed time: 0.003070981999999667 ms

```
 
Running the program with the Three privided files for random search produces the following result set: 
```text

Enter the search term: car
Search Method: 1)String Match 2)Regular Expression 3)Indexed 1

Search results: 
        french_armed_forces.txt - 0 matches
        hitchhikers.txt - 0 matches
        warp_drive.txt - 0 matches
Elapsed time: 0.0031996709999990713 ms

... 

Enter the search term: possible
Search Method: 1)String Match 2)Regular Expression 3)Indexed 2

Search results: 
        french_armed_forces.txt - 0 matches
        hitchhikers.txt - 0 matches
        warp_drive.txt - 0 matches
Elapsed time: 0.0010733549999990544 ms

...

Enter the search term: search
Search Method: 1)String Match 2)Regular Expression 3)Indexed 3

Search results: 
        french_armed_forces.txt - 0 matches
        hitchhikers.txt - 0 matches
        warp_drive.txt - 0 matches
Elapsed time: 1.5019000000116023e-05 ms

```

### Processing feedback 
A quick observation will point to the fact that Index Search is slower in this implementation. 
This result is counter-intuitive because memory access-access is supposed to be faster than parsing through a file. 
With smaller files, it should have been the fastest because file processing is I/O-bound while index access is CPU and RAM bound.
  
Because Python uses a single process by default, we could speed Search by Index by simple implementing multiprocessing. 
We can chunk up input data base on the number of agent and lunch multiple processes. 

We can leverage libraries, python has many libraries that probably address the issue of latency in file processing. 

we might need to switch from using the standard interpreter. PyPY is a good alternative.  

    
Run a performance test that does 2M searches with random search terms, and measures execution time. Which approach is fastest? Why?
Provide some thoughts on what you would do on the software or hardware side to make this program scale to handle massive content and/or very large request volume (5000 requests/second or more). 

### How to run the application
to execute the project just, download it and navigate to `target_word_search/Document_Search` directory. 
Make sure you have python3 install. If you do, run `$ python3 word_search.py` this should execute the program. 
If you want to run the unit test, navigate to `target_word_search/Document_Search/tests`, after that execute: 
 `$ pytest word_search_tests.py`. Here is sample test run. 
 
```text
$ pytest -v word_search_tests.py  
======================================================================================================================== test session starts =========================================================================================================================
platform darwin -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /Users/moise/.pyenv/versions/3.8.3/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/moise/Workspa"ce/target_word_search
collected 14 items                                                                                                                                                                                                                                                   

word_search_tests.py::test_search_by_simple_string_matching PASSED                                                                                                                                                                                             [  7%]
word_search_tests.py::test_search_by_simple_string_matching_no_match PASSED                                                                                                                                                                                    [ 14%]
word_search_tests.py::test_search_by_simple_string_matching_hitchhikers PASSED                                                                                                                                                                                 [ 21%]
word_search_tests.py::test_search_by_simple_string_matching_file_not_found_error PASSED                                                                                                                                                                        [ 28%]
word_search_tests.py::test_search_by_re_matching PASSED                                                                                                                                                                                                        [ 35%]
word_search_tests.py::test_search_by_re_matching_no_match PASSED                                                                                                                                                                                               [ 42%]
word_search_tests.py::test_search_by_re_matching_hitchhikers PASSED                                                                                                                                                                                            [ 50%]
word_search_tests.py::test_search_by_re_matching_file_not_found_error PASSED                                                                                                                                                                                   [ 57%]
word_search_tests.py::test_search_by_index_matching PASSED                                                                                                                                                                                                     [ 64%]
word_search_tests.py::test_search_by_index_no_match PASSED                                                                                                                                                                                                     [ 71%]
word_search_tests.py::test_search_by_index_hitchhikers PASSED                                                                                                                                                                                                  [ 78%]
word_search_tests.py::test_search_string_match PASSED                                                                                                                                                                                                          [ 85%]
word_search_tests.py::test_search_regex_match PASSED                                                                                                                                                                                                           [ 92%]
word_search_tests.py::test_search_index_match PASSED                                                                                                                                                                                                           [100%]

========================================================================================================================= 14 passed in 0.03s =========================================================================================================================
(
``` 

