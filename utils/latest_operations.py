import json
from datetime import datetime
list_of_operations = []

def open_file(file):
    with open(file, 'r', encoding='utf-8') as openfile:
        operations = json.load(openfile)
    return operations


list_of_operations = open_file('operations.json')
#print(list_of_operations[1])
#dict = list_of_operations[1]
#print(dict['date'])
#for key, value in list_of_operations[1]:
#    print(key, value)


def filtered_date(list):
    filtered = []
    for element in list:
        if element:
            operation = element
            #if operation['date']:
            operation['date'] = datetime.fromisoformat(element['date'])
            operation['date'] = operation['date'].strftime("%d.%m.%Y")
            #print(operation)
            filtered.append(operation)
            #print(filtered)
    return filtered


filtered_list = filtered_date(list_of_operations)
print(filtered_list)

