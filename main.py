def capital_letters(text):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    capital_alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    edited_text = ''

    for sym in text:
        if sym in alfabet:
            index1 = 0
            for letter in alfabet:
                index1 += 1
                if letter == sym:
                    break
            index2 = 0
            for letter in capital_alfabet:
                index2 += 1
                if index2 == index1:
                    edited_text += letter
        else:
            edited_text += sym

    return edited_text

def range_check(number, low_value, high_value):
    return low_value < number < high_value

def sym_count_check(text, delimiter):
    sym_count = 0
    delimiter_count = 0

    for sym in text:
        sym_count += 1
        if sym == delimiter:
            delimiter_count += 1

    return sym_count + delimiter_count

def item1_creating_new_flight():
    data_without_delimiter = ''

    print('Введите данные рейса:')
    flight_number = input('XXXX - номер рейса: ')
    while sym_count_check(flight_number, data_without_delimiter) != 4:
        print('ОШИБКА! Неверный формат ввода номера рейса.')
        flight_number = input('XXXX - номер рейса: ')
    flight_number = capital_letters(flight_number)

    flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')
    delimiter = '/'
    while sym_count_check(flight_date, delimiter) != 12:
        print('ОШИБКА! Неверный формат ввода даты.')
        flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')

    departure_time = input('ЧЧ:ММ - время вылета: ')
    delimiter = ':'
    while sym_count_check(departure_time, delimiter) != 6:
        print('ОШИБКА! Неверный формат ввода времени вылета.')
        departure_time = input('ЧЧ:ММ - время вылета: ')

    flight_duration = float(input('XX.XX - длительность перелета: '))
    while not range_check(flight_duration, 0, 100):
        print('ОШИБКА! Длительность перелёта должна быть неотрицательным двузначным числом!')
        flight_duration = float(input('XX.XX - длительность перелета: '))

    iata_code_departure = input('ХХХ - аэропорт вылета: ')
    while sym_count_check(iata_code_departure, data_without_delimiter) != 3:
        print('ОШИБКА! Неверный формат ввода аэропорта вылета.')
        iata_code_departure = input('ХХХ - аэропорт вылета: ')
    iata_code_departure = capital_letters(iata_code_departure)

    iata_code_arrival = input('ХХХ - аэропорт назначения: ')
    while sym_count_check(iata_code_arrival, data_without_delimiter) != 3:
        print('ОШИБКА! Неверный формат ввода аэропорта назначения.')
        iata_code_arrival = input('ХХХ - аэропорт назначения: ')
    iata_code_arrival = capital_letters(iata_code_arrival)

    ticket_price = float(input('.XX - стоимость билета( > 0): '))
    while ticket_price < 0:
        print('ОШИБКА! Стоимость билета не может быть отрицательной.')
        ticket_price = float(input('.XX - стоимость билета( > 0): '))

    if flight_duration < 10:
        flight = f'{flight_number} {flight_date} {departure_time} 0{flight_duration} {iata_code_departure} {iata_code_arrival} {ticket_price}'
    else:
        flight = f'{flight_number} {flight_date} {departure_time} {flight_duration} {iata_code_departure} {iata_code_arrival} {ticket_price}'
    print(f'\nИнформация о рейсе {flight}* добавлена\n')
    return flight

def item2_show_all_flights(text):
    flight = ''
    if text:
        for sym in text:
            if sym == ';':
                print(f'Информация о рейсе: {flight}')
                flight = ''
            else:
                flight += sym
    else:
        print('\nИнформация о рейсах отсутствует.')

def item3_search_flight(text):
    data_without_delimiter = ''
    searching_flight = input('Введите номер рейса в формате XXXX: ')
    while sym_count_check(searching_flight, data_without_delimiter) != 4:
        print('ОШИБКА! Неверный формат ввода номера рейса.')
        searching_flight = input('Введите номер рейса в формате XXXX: ')
    searching_flight = capital_letters(searching_flight)

    flight_data = ''
    flight_number = ''

    if not text:
        print('\nИнформация о рейсах отсутствует.')
        return

    for sym in text:
        if sym == ';':
            for number in flight_data:
                flight_number += number
                if flight_number == searching_flight:
                    print(f'Информация о рейсе: {flight_data}')
                    return
            flight_data = ''
            flight_number = ''
        else:
            flight_data += sym
    else:
        print('Информация о рейсе не найдена!')

def main_menu():
    all_flights = ''

    while True:
        print('\nГлавное меню:')
        print('1 - ввод рейса\n'
              '2 - вывод всех рейсов\n'
              '3 - поиск рейса по номеру\n'
              '0 - завершение работы')

        menu_item = int(input('\nВведите номер пункта меню: '))

        if menu_item == 1:
            all_flights += f'{item1_creating_new_flight()};'
        elif menu_item == 2:
            item2_show_all_flights(all_flights)
        elif menu_item == 3:
            item3_search_flight(all_flights)
        else:
            print('Завершение работы')
            return

print('Сервис поиска авиабилетов\n')
main_menu()
