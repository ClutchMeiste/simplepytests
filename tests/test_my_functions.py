import pytest
import my_functions as my_functions
import time

def test_add():
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2

def test_add_strongs():
    result = my_functions.add("Hello", " World")
    assert result == "Hello World"

@pytest.mark.slow        
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3    
    
@pytest.mark.xfail(reason="We know this test will fail bcz we cant devide by zero")
def test_divide_by_zero():
    assert my_functions.divide(number_one=10, number_two=0) == 0

