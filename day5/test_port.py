def f1():
    port=3000
    assert port == 3000

def f2():
    port=3000
    assert port>3000
    
def f3():
    app="insta"
    assert app == "insta"
    
    
def f4():
    n=100
    assert n<200
    
    
def sample():
    status_code=200
    assert status_code == 200
    
def sample_url():
    url="api.com"
    assert url == "api.com"