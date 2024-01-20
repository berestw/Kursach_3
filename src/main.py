from utils import *

values = get_executed_operations(load_json())
operations = sort_operations_date(values)
date = change_date(operations)
card_number = mask_card_number(operations)
amount_number = mask_amount_number(operations)


for operation in range(len(operations)):
    print(f"{date[operation]} {operations[operation]['description']}")
    print(f"{card_number[operation]} => Счёт {amount_number[operation]}")
    print(f"{operations[operation] ['operationAmount']['amount']} {operations[operation] ['operationAmount']['currency']['name']}\n")
