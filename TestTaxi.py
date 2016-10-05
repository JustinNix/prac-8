from Car import Taxi

prius_1 = Taxi("Prius 1", 100)

prius_1.drive(40)
print(prius_1)

prius_1.start_fare()
prius_1.drive(100)
print(str(prius_1) + "Costing " + str(prius_1.get_fare()))
