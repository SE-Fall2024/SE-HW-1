# test_binarySearch.py
from Binary_Search import binary_search

def test_binarySeach_pass():
    
    assert binary_search([1,4,6,8,10],8) == True  

def test_binarySeach_fail():
   
    assert binary_search([1,4,6,8,10],10) == True  
