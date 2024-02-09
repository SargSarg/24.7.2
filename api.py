import requests
import json
import os
class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/" #адрес сайта пет френдс

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password,
        }#Открываем api документацию и видим что емаил с паролем находятся в headers запроса
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text #на всякий случай если не вернет в json формате
        return status, result



    def post_api_create_pet_simple(self, auth_key, name, animal_type, age):
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
