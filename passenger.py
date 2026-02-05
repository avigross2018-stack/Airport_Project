import json
import string
import random

def load_avaliable_lines(path):
    with open(path) as json_file:
         data = json.load(json_file)
    return data["available_line"]

# x = load_avaliable_lines()
# print(load_avaliable_lines())



def show_lines(lines):
    print('Available flights:')
    for i,line in enumerate(lines,start=1):
        origin = line['Origin_airport']
        destination = line['Destination_airport']
        print(f'{i}. {origin} -> {destination}')

# show_lines(x)
def chose_line(lines):
    index = len(lines)
    while True:
        choice=input('Enter your line ')
        try:
            if int(choice) > 0 and int(choice) <= index:
                selected=lines[int(choice) -1]
                print (f'You select the line:{selected['Origin_airport']} -> {selected['Destination_airport']} ')
                break
            else:
                print('Invalid value')
                continue
        except ValueError:
            print('Invalid value')
            continue


def passenger_unit(path):
    lines=load_avaliable_lines(path)
    show_lines(lines)
    chose_line(lines)


def ticket_id():
    letters = list(string.ascii_letters)
    symbols = list(string.punctuation)
    numbers = list(string.digits)
    random_list = letters + symbols + numbers
    random_id = random.choices(random_list, k=8)
    print(''.join(random_id))

