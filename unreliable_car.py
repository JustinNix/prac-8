from Car import UnreliableCar

ford = UnreliableCar("Ford 2012", 100, 50)
holden = UnreliableCar("Holden 2012", 100, 25)

ford.drive(50)
print(ford)

holden.drive(500)
print(holden)