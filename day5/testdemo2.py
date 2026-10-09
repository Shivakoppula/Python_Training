import pytest
@pytest.mark.integration
def testdb():
    assert True
    
@pytest.mark.slow
def testslowprocessing():
    assert True
    
def testfix():
    assert True
    