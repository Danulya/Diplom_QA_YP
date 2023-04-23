import data
import sender_stand_request2


# Функция для проверки успешного создания заказа и получения заказа по треку
def positive_assert():
    # В переменную current_body копируем данные для создания заказа из словаря data
    current_body = data.order_body.copy()
    # В переменную order_response сохраняем результат запроса на создание заказа:
    order_response = sender_stand_request2.post_new_order(current_body)
    # В тело ответа сохраняем результат запроса на создание заказа в формате json
    response_body = order_response.json()["track"]
    # В переменную get_order_response сохраняем результат запроса заказа по треку
    get_order_response = sender_stand_request2.get_order_by_track()

    print(response_body)
    print(get_order_response.json())

    # Проверяем, что в ответе есть поле track, и оно не пустое
    assert order_response.json()["track"] != ""
    # Проверяем, что код ответа равен 200
    assert get_order_response.status_code == 200

 # Тест  на получение данных заказа по трек-номеру
def test_get_order_request_by_track():
    positive_assert()