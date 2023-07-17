import json
from datetime import datetime


def get_data(file='operations.json'):
    with open(file, encoding="UTF-8") as json_file:
        return json.load(json_file)

#abkmnh executed
def get_filtered_data(data):
    new_data = []
    for transaction in data:
        if transaction.get('state') == 'EXECUTED':
            new_data.append(transaction)
    return new_data

#сортировка по дате и вывод 5 операций
def get_sorted_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

#Формат даты
def get_formatted(date):
    date_transaction = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date_transaction = date_transaction.strftime("%d.%m.%Y")
    return (date_transaction)


def masking_card(card_info: str):
    """
    :param card_info: строка с именем и номером карты/счета
    :return: имя карты/счета и ее замаскированный номер
    """
    if len(card_info) != 0:
        card_number = card_info.split()[-1]
        card_name = ' '.join(card_info.split()[:-1])

    if len(card_number) == 16 and card_number.isdigit():
        card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]

    elif len(card_number) == 20 and card_number.isdigit():
        card_number = '**' + card_number[-4:]

    else:
        return 'Uncorrected card_info'

    return f'{card_name} {card_number}'


def masking_card2(card_info: str):
    if card_info.startswith('Счет'):
        return 'Счет ****' + card_info[-4:0]
