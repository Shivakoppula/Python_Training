import pytest

@pytest.fixture
def input():
    var = 40
    return var

def test_input(input):
    assert input%3==0
    
    
def test(input):
    assert input%6==0
    
