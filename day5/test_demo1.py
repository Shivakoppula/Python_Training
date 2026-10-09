import pytest



@pytest.mark.skip
def test():
    assert 100+50==150
    
def add():
    assert 10+20==30
    
def sub():
    assert 20-10==10

def mul():
    assert 10*5==50
    
    
@pytest.mark.skipif(sys.platform!="linux",reason="Skipping on non-Linux platforms")
def testlinux():
    assert True
    
@pytest.mark.xfail(reason="Expected to fail")
def testxfail():
    assert 10-5==10