'''Create a Python file called holiday.py in your folder.
● You will need to create four functions:
● hotel_cost — This function will take the number of nights a user
will be staying at a hotel as an argument, and return a total cost for
the hotel stay (You can choose the price per night charged at the
hotel).

● plane_cost — This function will take the city you are flying to as an
argument and return a cost for the flight (Hint: use if/else if
statements in the function to retrieve a price based on the chosen
city).

● car_rental — This function will take the number of days the car will
be hired for as an argument and return the total cost of the car
rental.
● holiday_cost — This function will take three arguments: the
number of nights a user will be staying in a hotel, the city the user
will be flying to, and the number of days that the user will be hiring
a car for. Using these three arguments, you can call all three of the
above functions with respective arguments and finally return a
total cost for your holiday.
● Print out all the details about the holiday in a meaningful way!
● Try using your program with different combinations of input to show its
compatibility with different options'''

# first define functions to calculate costs of the hotel, flight and the rent a car, adding parametars such as prices
# with choices of cities and type of car rentals
#when asking for the input of cities and car types .title() function is applied to the user's input so that it will match
# conditional in the if statements to determine which rate to apply

def hotel_cost(nights):
    cost = nights * 115
    return cost

def plane_cost(city):

    while True:
        if city == 'Detroit' or city == 'Philadelphia':
            return 259
        elif city == 'New York' or city == 'Baltimore':
            return 350
        else:
            city = input('No flights to this city. please choose from: Detroit, Philadelphia, New York or Baltimore: ').title()
            continue

def car_cost(car_type, days):
    #rental = car_type * days

    while True:

        if car_type == 'Economy':
            car_type = 25
        elif car_type == 'Family':
            car_type = 40
        elif car_type == 'Executive':
            car_type = 60
        else:
            print('You have entered the wrong choice, please select one of the three options: ')
            car_type = input('Please select your car for rental: Economy, Family or Executive: ').title()
            continue
        return car_type * days

#finally total holiday cost is defined by taking all he predefined costs and thier parametres
# into variables: hotel, plane and car and adding them up into a total that is returned when holiday_cost function
#is called in the final print out

def holiday_cost():
    nights = int(input('Please enter how many nights are you staying: '))
    hotel = hotel_cost(nights)
    print('Total cost of your hotel accommodation is: ' + str(hotel) + ' USD.')

    city = input('Which city are you flying to: New York, Baltimore, Detroit or Philadelphia: ').title()
    plane = plane_cost(city)
    print("Tho cost of your flight is: " + str(plane) + ' USD.')

    days = int(input('How many days you are renting the car for: '))
    car_type = input('Please select your car for rental: Economy, Family or Executive: ').title()
    car = car_cost(car_type, days)
    print(f'The cost of your car rental is: {car} USD.')

    total = hotel + plane + car

    return total


print(f'Total cost of your holiday is: {holiday_cost()} USD.')