def calculator_base_price(origin_airport,destination_airport):
    calc_price = (origin_airport + destination_airport) / 400
    return calc_price
calc = calculator_base_price(400,400)
print(calc)
