import pytest
import json
import utils


from utils import latest_operations

@pytest.fixture
def list():
    return [
      {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
          "amount": "41096.24",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
      },
      {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
          "amount": "67314.70",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
      }]

json_file = 'C:\\Users\\Кекета\\PycharmProjects\\kursovayaBackend\\tests\\testfile.json'

def test_open_file():
    assert latest_operations.open_file(json_file) == [{"test1": 1, "test2": 2}]

def test_exec_only(list):
  assert latest_operations.exec_only(list) == [{
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
          "amount": "41096.24",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
      }]

def test_rebuild_list(list):
  assert latest_operations.rebuild_list(list) == [
    {'date': '08.12.2019',
     'description': 'Открытие вклада',
     'from': 'Отсутствует',
     'to': 'Счет 90424923579946435907',
     'amount': '41096.24',
     'currency': 'USD'
     },
    {'date': '12.09.2018',
     'description': 'Перевод организации',
     'from': 'Visa Platinum 1246377376343588',
     'to': 'Счет 14211924144426031657', 'amount':
       '67314.70',
     'currency': 'руб.'
     }
  ]

def test_hidden_number(list):
  assert latest_operations.hidden_number(list) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет **5907', 'from': 'Отсутствует'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246 7** **** 3588', 'to': 'Счет **1657'}]