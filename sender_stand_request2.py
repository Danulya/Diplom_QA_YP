import requests
import configuration
import data


# Функция для создания нового заказа
def post_new_order(body):
    # Обращаясь к функции Post передаем полный путь
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER_PATH,
                         json=body,  # тело
                         headers=data.headers)  # заголовок запроса


# В переменную response сохраняется результат запроса на создание заказа
response = post_new_order(data.order_body)
# Выводим на экран код ответа
print(response.status_code)
# Выводим на экран тело ответа
print(response.json())


# Функция для получения трек-номера заказа и его сохранения
def get_new_order_track():
    # В переменную new_order_track сохраняется обновлённое тело
    new_order_track = post_new_order(data.order_body)
    # В переменную order_track сохраняется номер трека заказа
    order_track = new_order_track.json()["track"]
    # Возвращает трек заказа
    return order_track


# Функция запроса данных заказа по треку заказа
def get_order_by_track():
    # В переменную order_track сохраняется результат запроса на получение трека
    order_track = get_new_order_track()
    track_dict = data.order_track.copy()
    track_dict["track"] = order_track
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,  # передаем полный путь
                        params=track_dict)  # заголовки


print(response.json())
