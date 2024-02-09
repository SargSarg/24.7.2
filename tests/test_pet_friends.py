import pytest
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, absence_email, absence_password

pf = PetFriends() #добавляем переменную

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password) #результат сохранится в переменные ресалт и статус
    assert status == 200 #проверяем что статус 200
    assert 'key' in result #потому что в ответе должен присутствовать key как видно в api документации


def test_get_api_key_for_absence_email_and_password(email=absence_email, password=absence_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_email_and_password(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_absenc_email(email=absence_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_absence_password(email=valid_email, password=absence_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_post_create_simple():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, 'Васёк', 'Утка', '5')
    assert status == 200
    assert result['name'] == 'Васёк'
    assert result['animal_type'] == 'Утка'
    assert result['age'] == '5'


def test_post_create_simple_invalid_name():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, '123', 'Утка', '5')
    assert status == 200
    assert result['name'] != '123'
    assert result['animal_type'] == 'Утка'
    assert result['age'] == '5'

def test_post_create_simple_invalid_animal_type():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, 'Васёк', '123', '5')
    assert status == 200
    assert result['name'] == 'Васёк'
    assert result['animal_type'] != '123'
    assert result['age'] == '5'

def test_post_create_simple_invalid_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, 'Васёк', 'Утка', 'оттт')
    assert status == 200
    assert result['name'] == 'Васёк'
    assert result['animal_type'] == '123'
    assert result['age'] != 'оттт'
