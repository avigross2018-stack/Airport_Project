import json
import csv
from pathlib import Path
def read_csv(path):
    csv_lines = []
    with open(path, 'r') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            csv_lines.append(line)
    return csv_lines

def return_budget_amount(path):
    try:
        with open(path, "r") as f:
            str_amount = f.read()
            return float(str_amount)
    except Exception as e:
        print(f"error! type error:{e}")

def update_budget_file(amount, path):
    with open(path, 'w') as f:
        f.seek(0)
        file = f.write(str(amount))
    print(f'The budget was update. the budget is: {amount}')

def read_airports_file(path):
    airports_list = []
    with open(path, 'r') as f:
        airports = csv.DictReader(f)
        for row in airports:
            airports_list.append(dict(row))
    return airports_list



def check_exist_airport(airports_file_path, origin_airport_code, target_airport_code):
    airport_dict = read_airports_file(airports_file_path)
    valid_if_exist = 0  #if equal 2 the airports exists else one or both doesn't exist
    for airport in airport_dict:
        if origin_airport_code.upper() in airport['airport_code']:
            valid_if_exist += 1
        if target_airport_code.upper() in airport['airport_code']:
            valid_if_exist += 1
    if valid_if_exist == 2:
        return True
    return False

def add_airline_to_available_flights(js_path, origin_airport_code, target_airport_code):
    # if the airline doesn't exist the new airline will add, else the func will return msg
    available_airline = {}
    with open(js_path, 'r') as f:
        available_airline = json.load(f)
    if {'Origin_airport': origin_airport_code.upper(), 'Destination_airport': target_airport_code.upper()} in available_airline['available_line']:
        return 'The line already exist'
    else:
        available_airline["available_line"].append({"Origin_airport" : origin_airport_code.upper(), "Destination_airport" : target_airport_code.upper()})
        available_airline["available_line"].append({"Origin_airport" : target_airport_code.upper(), "Destination_airport" : origin_airport_code.upper()})
        with open(js_path, 'w') as f:
            f.seek(0)
            json.dump(available_airline, f)
            f.truncate()
        return "The airline added to you available flights"
    

def compare_budget_to_price(origin_airport_code, target_airport_code, airport_price_path, budget_path, available_flights_file):
    amount_bud = return_budget_amount(budget_path)
    airports_list = read_airports_file(airport_price_path)
    origin_airports_price = 0
    target_airports_price = 0
    final_price = 0
    for i in range(len(airports_list)):
        if airports_list[i]["airport_code"] == origin_airport_code.upper():
            origin_airports_price = int(airports_list[i]["entry_fee_usd"])
    for i in range(len(airports_list)):
        if airports_list[i]["airport_code"] == target_airport_code.upper():
            target_airports_price = int(airports_list[i]["entry_fee_usd"])
    final_price = origin_airports_price + target_airports_price
    if amount_bud > final_price:       
        adding_airline = add_airline_to_available_flights(available_flights_file, origin_airport_code, target_airport_code)
        if adding_airline == 'The line already exist':
            print('The line already exist')
            # return 'The line already exist'
        elif adding_airline == "The airline added to you available flights":
            while True:        
                valid = input("you have enough money. \nDo you want to perch \n1) Yes \n2) No\n")
                if valid == '1':
                    return update_budget_file(amount_bud - final_price, budget_path)
                    
                elif valid == '2':
                    return 'Perch cancel'
                else:
                    print('Wrong input')
                    continue
    elif amount_bud < final_price:
        return 'There is not enough money'
            


        
# budget_file = Path('./budget.txt')
# js = Path('./available_flights.json')
# cs = Path('./airport_entry_fee.csv')
# # print(check_exist_airport(js, cs, 'lax', 'jfk'))

# print(compare_budget_to_price('lax','jfk',cs,budget_file,js))