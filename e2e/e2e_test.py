import requests


url = 'http://172.17.0.1:8080/'


def test_index():
    resp = requests.get(url)
    assert resp.status_code == 200
