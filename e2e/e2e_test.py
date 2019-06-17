import requests


url = 'http://172.17.0.1:8080/'


def test_healthz():
    resp = requests.get(url + 'healthz')
    assert resp.status_code == 200
