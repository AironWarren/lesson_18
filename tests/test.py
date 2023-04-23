import requests
from datetime import date
from requests import Response
import pytest
from pytest_voluptuous import S

from schemas.reqres_in import number_user_schema, list_users_schema

url = 'https://reqres.in/api/'


@pytest.mark.parametrize("path_part", ["users", "unknown", "register", "login"])
def test_status_code(path_part):
    response: Response = requests.get(url + f'{path_part}')
    assert response.status_code == 200


def test_single_user_validate_schema():
    response: Response = requests.get(url + 'users/2')
    assert S(number_user_schema) == response.json()


def test_get_resource_page_number():
    response: Response = requests.get(url + 'unknown')
    assert response.json()['page'] == 1


def test_get_len_date_resource():
    response: Response = requests.get(url + 'unknown')
    len_date_resource = response.json()['per_page']
    assert len(response.json()['data']) == len_date_resource == 6


def test_post_new_user():
    new_user = {
        "name": "morpheus",
        "job": "leader"
    }
    response: Response = requests.post(url + 'users', json=new_user)

    assert response.status_code == 201


def test_update_user_put():
    update_user = {
        "name": "neo",
        "job": "senior"
    }

    response: Response = requests.put(url + 'users/2', json=update_user)

    assert response.status_code == 200


def test_update_user_patch():
    update_user = {
        "name": "trinity"
    }

    response: Response = requests.patch(url + 'users/2', json=update_user)

    assert response.json()['name'] == 'trinity'


def test_delete_user():
    response: Response = requests.delete(url + 'users/2')

    assert response.status_code == 204


def test_new_user_date():
    new_user = {
        "name": "morpheus",
        "job": "leader"
    }
    response: Response = requests.post(url + 'users', json=new_user)

    assert response.json()['createdAt'][0:10] == str(date.today())
