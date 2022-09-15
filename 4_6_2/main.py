# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# Пример положительных тестов:
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.



import requests

token =
url = 'https://cloud-api.yandex.net/v1/disk/resources/'
folder = 'CHECK_PYTHON_8'

def create_folder(token, url, folder):
    '''Метод создает папку на Я.Д.'''
    params = {'path': folder}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    return requests.put(url, headers=headers, params=params)


  
   

# if __name__ == '__main__':

#     create_folder(token, url, folder)
    
    
#     print('Конец программы.')