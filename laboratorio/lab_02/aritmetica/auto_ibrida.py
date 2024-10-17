DIST_YEARLY_KM: float = 30_000

class Car:
    def __init__(self, *args):
        self.cost = float(args[0])
        self.distance_yearly = float(args[1])
        self.fuel_efficiency = float(args[2])
        self.resell_price = float(args[3])

    def expected_cost(self, years: int, fuel_cost: float):
        yearly_fuel_cost = ( fuel_cost * self.distance_yearly / self.fuel_efficiency )

        return self.cost + (yearly_fuel_cost * years) - self.resell_price

def main():
    fuel_cost = input("Inserisci il costo del carburante (al litro) [EUR]: ")
    print() # Separatore

    car_cost = input("Inserisci il costo dell'auto [EUR]: ")
    distance_yearly = input("Inserisci la distanza annuale percorsa (estimativa) [km]: ")
    fuel_efficiency = input("Inserisci l'efficienza del carburante (in `km/L`) [km]: ")
    resell_price = input("Inserisci il valore (estimativo) di rivendita dell'auto dopo 5 anni [EUR]: ")

    car = Car(car_cost, distance_yearly, fuel_efficiency, resell_price)

    print(f"Costo totale di proprietà (per 5 anni): { car.expected_cost(5, float(fuel_cost)) } EUR")

if __name__ == "__main__":
    main()