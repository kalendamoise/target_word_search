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

A quick observation will point to the fact that Index Search is slower in this implementation. 
This result is counter-intuitive because memory access-access is supposed to be faster than parsing through a file. 
With smaller files, it should have been the fastest.  

    
Run a performance test that does 2M searches with random search terms, and measures execution time. Which approach is fastest? Why?
Provide some thoughts on what you would do on the software or hardware side to make this program scale to handle massive content and/or very large request volume (5000 requests/second or more). 
