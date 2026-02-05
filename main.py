from checking_functions import manager_authentication, file_exist
from pathlib import Path
from actions_on_files import read_csv
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
        user = input('please choise, to manager press: 1: to passenger press: 2:')
        if user == '1':
            manager_name = input('please enter your name: ')
            manager_pw = input('please enter your password: ')
            cred_list = read_csv(credentials_file)
            check_manager_info = manager_authentication(manager_name, manager_pw, cred_list)
            if check_manager_info == False:
                return 'Incorrect user name, or password'
            
            flag = True
        elif user == '2':
            flag = True
            passenger_unit(available_flights_file)
            print('Your ticket id is')
            print(ticket_id())
        else:
            print('Invalid input')
            continue

              







menu()
