from Car import SilverServiceTaxi
from Car import Taxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    running_cost = 0
    menu_choice = input("q)uit, c)hoose taxi, d)drive \n >>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            car_count = 0
            for vehicle in taxis:
                print("{} {}".format(car_count, vehicle))
                car_count += 1
            taxi_choice = int(input("Choose your taxi: "))
            chosen_taxi = taxis[taxi_choice]
            print("Bill to date: {}".format(running_cost))
        menu_choice = input("q)uit, c)hoose taxi, d)drive \n >>> ").lower()

        if menu_choice == "d":
            distance = int(input("Drive how far? "))
            chosen_taxi.start_fare()
            chosen_taxi.drive(distance)
            print("your trip cost you {}".format(chosen_taxi.get_fare())) #TODO FIX THIS PRINT STATEMENT WHEN I FIX Car.py
            running_cost += chosen_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(running_cost))
        menu_choice = input("q)uit, c)hoose taxi, d)drive \n >>> ").lower()
    else:
        print("Total trip cost: {}".format(running_cost))
        print("taxis are now: ")
        car_count = 0
        for vehicle in taxis:
            print("{} {}".format(car_count, vehicle))
            car_count += 1


main()