import csv
from pathlib import Path
from actions_on_files import read_airports_file
def price_calc(origin_airport_code, target_airport_code, base_price):
    origin_continent = False
    target_continent = False
    airport_entry_file = Path('./airport_entry_fee.csv')
    airports = read_airports_file(airport_entry_file)#מחזיר רשימה של מילונים
    for a_dict in airports:
        if a_dict["airport_code"] == origin_airport_code:
            origin_continent = a_dict["continent"]
    for a_dict in airports:
        if a_dict["airport_code"] == target_airport_code:
            target_continent = a_dict["continent"]
    if origin_continent and target_continent:
        continents_pricing_file = Path('./continents_pricing.csv')
        continents_pricing = read_airports_file(continents_pricing_file)#מחזיר רשימה של מילונים
        for a_dict in continents_pricing:
            if a_dict["source_continent"] == origin_continent and a_dict["target_continent"] == target_continent:
                extra_price = int(a_dict["base_price_usd"]) / 400
                base_price += extra_price
    return base_price