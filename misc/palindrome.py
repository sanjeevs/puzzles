"""Check whether the list is a palindrome."""

def palindrome(lst):
    print("palindrome", lst)
    if len(lst) <= 1:
        return True
    else:
        return (lst[0] == lst[-1]) and palindrome(lst[1:-1])

def test_palindrome_0():
    assert palindrome([]) == True

def test_palindrome_1():
    assert palindrome([0]) == True

def test_palindrome_2():
    assert palindrome([0,0]) == True
    assert palindrome([0,1]) == False 

def test_palindrome_6():
    assert palindrome([0,1,2,2,1,0]) == True
