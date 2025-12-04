import requests

def test_homepage_status_code():

    url = "https://www.vinegret.cz/"
    response = requests.get(url)
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"

