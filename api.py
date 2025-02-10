import requests
import json

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"
    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к Api сервера и возвращает статус запроса и результат в формате
         JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers = headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_list_of_pets(self, auth_key: json, filter: str = "" ):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком найденных питомцев, совпадающих с фильтром"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def add_new_pet_with_valid_data(self, auth_key: json, name: str, animal_type: str, age: int, pet_photo: str = ""):
        """Метод делает запрос к API сервера и позволяет добавлять на сайт новый пост о животном с его фотографией"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id, name, animal_type, age):
        """Метод делает запрос к API сервера и позволяет обновлять информацию о животном"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data, params=pet_id)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_database(self, auth_key: json, pet_id):
        """Метод делает запрос к API сервера и позволяет удалять собственный пост о животном"""
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers, params=pet_id)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_pet_simple_with_valid_data(self, auth_key: json, name: str, animal_type: str, age: int):
        """Метод делает запрос к API сервера и позволяет добавлять на сайт новый пост о животном без его фотографии"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def set_photo_of_pet(self, auth_key: json, pet_id, pet_photo: str = ""):
        """Метод делает запрос к API сервера и добавляет фото к посту о животном"""

        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, params=pet_id, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result