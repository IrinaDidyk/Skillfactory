from api import PetFriends
from settings import valid_email, valid_password, not_valid_email, not_valid_password
import pytest
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_not_valid_user(email = not_valid_email, password = valid_password):
    status, result = pf.get_api_key(email,password)
    assert status != 200


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_with_not_valid_key(filter=''):
    status, auth_key = pf.get_api_key(valid_email, not_valid_password)
    assert status != 200, f"Ошибка аутентификации: {auth_key}"

    with pytest.raises(TypeError):
        status, result = pf.get_list_of_pets(auth_key, filter)


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                    age='4', pet_photo='images/123456.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_valid_data(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_not_valid_data(name='', animal_type='',
                                    age='', pet_photo=''):
    status, auth_key = pf.get_api_key(not_valid_email, valid_password)
    assert status != 200, f"Ошибка аутентификации: {auth_key}"

    with pytest.raises(TypeError):
        status, result = pf.add_new_pet_with_valid_data(auth_key, name, animal_type, age, pet_photo)

def test_update_self_pet_info(name='AAA', animal_type='кто-то', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter = "my_pets")
    pet_id = my_pets['pets'][0]['id']

    if len(my_pets['pets'])>0:
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')

def test_delete_pet_from_database():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.delete_pet_from_database(auth_key, pet_id)
    assert status == 200

def test_create_pet_simple_with_valid_data(name='Ya', animal_type='двор',
                                    age='-4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple_with_valid_data(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_not_valid_data(name='', animal_type='',
                                    age=''):
    status, auth_key = pf.get_api_key(valid_email, not_valid_password)
    assert status != 200, f"Ошибка аутентификации: {auth_key}"

    with pytest.raises(TypeError):
        status, result = pf.create_pet_simple_with_valid_data(auth_key, name, animal_type, age)


def test_set_photo_of_my_pet(pet_photo='images/123456.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.set_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200

def test_set_non_existent_photo_of_my_pet(pet_photo='images/ergrujdchzfgarysyjudxfharaershysfhsdysrtyu.jpg'):
    with pytest.raises(FileNotFoundError):
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.set_photo_of_pet(auth_key, pet_id, pet_photo)

