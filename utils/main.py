from latest_operations import open_file, exec_only, rebuild_list,hidden_number

transaction_list = open_file('operations.json')
executed_list = exec_only(transaction_list)
rebuilt_list = rebuild_list(executed_list)
hidden_list = hidden_number(rebuilt_list)

for element in hidden_list[0:5]:
    print(f'{element["date"]} {element["description"]} \n{element["from"]} -> {element["to"]} \n{element["amount"]} {element["currency"]}')