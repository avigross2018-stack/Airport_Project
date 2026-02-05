import json

def load_avaliable_lines():
    with open('available_flights.json') as json_file:
         data = json.load(json_file)
    return data['available_lines']



def show_lines(lines):
    print('available flights:')
    for i,line in enumerate(lines,start=1):
        origin = line['origin_airport']
        destination = line['destination_airport']
        print(f'{i}. {origin} -> {destination}')


def chose_line(lines):
    choice=int(input('Enter your line '))
    selected=lines[choice-1]
    print (f'you selct the line:{selected['origin_airport']} -> {selected['destination_airport']} ')


def passenger_unit():
    lines=load_avaliable_lines()
    show_lines(lines)
    chose_line(lines)


# passenger_unit()