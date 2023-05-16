import json

from datetime import datetime

def open_file(file):
    with open(file, 'r', encoding='utf-8') as openfile:
        operations = json.load(openfile)
    return operations

def exec_only(list):
    exec_list = []
    for element in list:
        if element and element['state'] == "EXECUTED":
            exec_list.append(element)
    return exec_list

def rebuild_list(list):
    new_list = []
    for element in list:
        if element:
            new_dict = {}
            new_dict["date"] = datetime.fromisoformat(element['date']).strftime("%d.%m.%Y")
            new_dict["description"] = element["description"]
            try:
                new_dict["from"] = element["from"]
            except KeyError:
                new_dict["from"] = "Отсутствует"
            new_dict["to"] = element["to"]
            new_dict["amount"] = element["operationAmount"]["amount"]
            new_dict["currency"] = element["operationAmount"]["currency"]["name"]
            new_list.append(new_dict)
    return(sorted(new_list, key = lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True))


def hidden_number(list):
    hidden_list = []
    for element in list:
        if element:
            new_element = element
            try:
                if len(new_element['from']) == 25:
                    new_element['from'] = f"Счет **{new_element['from'][-4:]}"
                elif new_element['from'] == "Отсутствует":
                    new_element['from'] == "Отсутствует"
                else:
                    new_element['from'] = f"{new_element['from'][:-12]} {new_element['from'][-11:-10]}** **** {new_element['from'][-4:]}"
            except KeyError:
                new_element['from'] = "Отсутствует"
            if len(new_element['to']) == 25:
                new_element['to'] = f"Счет **{new_element['to'][-4:]}"
            else:
                new_element['to'] = f"{new_element['to'][:-12]} {new_element['to'][-11:-10]}** **** {new_element['to'][-4:]}"
            hidden_list.append(new_element)
    return hidden_list
