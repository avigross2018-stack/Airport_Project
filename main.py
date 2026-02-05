from checking_functions import manager_authentication, file_exist
from pathlib import Path
from actions_on_files import read_csv, add_airline_to_available_flights,compare_budget_to_price, check_exist_airport
from passenger import passenger_unit, ticket_id



budget_file = Path('./budget.txt')
airport_entry_file = Path('./airport_entry_fee.csv')
continents_pricing_file = Path('./continents_pricing.csv')
credentials_file = Path('./credential.csv')
available_flights_file = Path('./available_flights.json')

def menu():
    bud_check = file_exist(budget_file)
    cred_check = file_exist(credentials_file)
    if bud_check == False or cred_check == False:
        return "One of the files or both doesn't exist"
    flag = False
    while flag == False:
        user = input('Please choice, \nTo manager press: 1: \nTo passenger press: 2:\n')
        if user == '1':
            manager_name = input('Please enter your name: ')
            manager_pw = input('Please enter your password: ')
            cred_list = read_csv(credentials_file)
            check_manager_info = manager_authentication(manager_name, manager_pw, cred_list)
            if check_manager_info == False:
                return 'Incorrect user name, or password'
            elif check_manager_info == True:
                manager_add = input('For adding new airline enter 1:\n')
                if manager_add == '1':
                    origin_airport = input('Please enter the origin airport code: ')
                    target_airport = input('Please enter the destination airport code: ')
                    checking = check_exist_airport(airport_entry_file, origin_airport, target_airport)
                    if checking == True:
                        compare_budget_to_price(origin_airport, target_airport, airport_entry_file, budget_file, available_flights_file)
                    else:
                        print('There is no airport with that name.')
                        continue           
            flag = True
        elif user == '2':
            flag = True
            passenger_unit(available_flights_file)
            print('Your ticket id is')
            ticket_id()
        else:
            print('Invalid input')
            continue

              







menu()
