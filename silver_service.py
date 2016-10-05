from Car import SilverServiceTaxi

fancy_car = SilverServiceTaxi("Fancy Car", 100, 2)

fancy_car.start_fare()
fancy_car.drive(10)
print(str(fancy_car) + "costing " + str(fancy_car.get_fare()))

#TODO FIX THIS PRINT STATEMENT WHEN I FIX Car.py