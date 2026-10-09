import pytest

import request



@pytest.fixture
def api_url():
    url = "https://api.example.com"
    r=request.get(url)
    code=r.status_code
    return code

def test_api_status(get_url):
    assert get_url == 200