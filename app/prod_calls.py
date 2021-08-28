import requests

endpoint = 'https://linode.tryfastapi.com/entries/'

client = requests


def test_entries_list():
    response = client.get(endpoint) 
    assert response.status_code == 200
    # assert len(response.json()) == 2

def test_entries_create():
    response = client.post(endpoint, json={"title": "Hello world"}) 
    print(response.json())
    assert response.status_code == 201
    # assert len(response.json().keys()) == 2

def test_entries_create_invalid():
    response = client.post(endpoint, json={"content": "Hello world"}) 
    assert response.status_code == 422


if __name__ == "__main__":
    test_entries_create()

