import pytest
import requests

base_url = "https://ru.yougile.com/api-v2"


@pytest.fixture
def get_token():
    token = "9r0R3Abe5HhSwORlQdaFagEPdedES4wYkKG-Mghz1YtS1Wx1FckRwZUqKLi2Fwc4"
    return token


def test_get_projects(get_token):
    he = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {get_token}"
    }
    rest = requests.get(base_url+'/projects', headers=he)
    assert rest.status_code == 200

def test_create_project(get_token):
    he = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token}"
        }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)

    assert response.status_code == 201
    id = requests.get(base_url+"/projects/" + response.json()['id'], headers=he).json()['id']
    assert id == response.json()['id']

def test_change_data(get_token):
    he = {
    "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token}"
     }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)
    body = {
    "title": "проект new"
    }
    response_change = requests.put(base_url+"/projects/" + response.json()['id'], headers=he, json=body)
    title = requests.get(base_url+"/projects/" + response.json()['id'], headers=he).json()["title"]
    assert title == "проект new"

def test_negative():
    he = {
        "Content-Type": "application/json"
        }
    body = {
        "title": "проект dz4.",
        "users": {"7f5a9548-a400-4cf9-9eb2-ab7740ed0a02": "admin"}
        }
    response = requests.post(base_url+"/projects", headers=he, json=body)

    assert response.status_code == 401