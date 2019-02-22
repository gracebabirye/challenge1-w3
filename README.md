# WEEK 3
## ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Challenge one`
### * Sorting:
Given a list containing integers, floats and one character strings, write a function that takes a list and returns a dictionary with keys evens, odds, and
chars. The value for evens is a list of sorted even numbers, the value for odds is a list of sorted odd numbers and chars is a list of sorted character
strings. 

list_sort( [ 2, 0, 6, 5, 1, 7, ’ z’ , ’ a’ ] ) # returns { ‘ evens’ : [ 0, 2, 6] , odds: [ 1, 5, 7] , chars: [ ‘ a’ , ’ z’ ] } 

In the listsort folder there are two files list_sort. py and list_sort_test. py, list_sort_test. py includes minimal tests for
the challenge, implement list_sort( ) in list_sort. py to pass all the tests. Feel free to write more tests.

Create a new repository for the solution and copy over the challenge files to the new repository. You are expected to use version control and share a link
to the remote repository with your Learning facilitator for review.

<b> How to run the tests: </b> <br>
Navigate to the listsort folder in the terminal(command prompt) and run “pytest”( type pytest and press enter).

### * Extra challenge
Write a python program to find missing numbers from a list. Follow a test driven approach while completing this challenge
#### Example
Input : [ 1, 2, 3, 5, 6, 7, 9] <br>
Output: [ 4, 8]


## ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Challenge two`
### Object Oriented Programming(OOP)
### Bank account
A bank account can be accessed in multiple ways. Clients can make deposits and withdrawals using the internet, mobile phones, etc. Shops
can charge against the account.<br>

It should be possible to close an account; operations against a closed account must fail.<br>

In account. py there is a skeleton of the bankAccount class with unimplemented methods and in tests. py there are tests for the methods
in the bankAccount class. The challenge is to implement the methods.
