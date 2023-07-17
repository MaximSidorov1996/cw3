from utils import get_data, get_sorted_data, get_filtered_data, get_formatted, masking_card, masking_card2


def main():
    print("курсовая")
    data = get_data()
    data = get_filtered_data(data)
    data = get_sorted_data(data)


    for row  in data:
        print(get_formatted(row['date']),end=' ')
        print(row['description'])
        print(masking_card(row['to']))
        print(row['operationAmount']['amount'],row['operationAmount']['currency']['name'])


if __name__ ==  '__main__':
    main()

