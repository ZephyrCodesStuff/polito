from math import pow

AIR_DENSITY = 1.23
AIR_RESISTANCE = 0.2
CAR_AREA = 2.5
HP_TO_WATT_RATIO = 1 / 745.7

def resistance(speed: float):
    return 1/2 * AIR_DENSITY * pow(speed, 2) * CAR_AREA * AIR_RESISTANCE

def power_watt(resistance: float, speed: float):
    return resistance * speed

def power_hp(resistance: float, speed: float):
    return power_watt(resistance, speed) * HP_TO_WATT_RATIO

def main():
    speed = input("Inserisci il valore della velocità dell'auto (m/s): ")

    try:
        speed = float(speed)
    except ValueError:
        print("Il valore immesso non è un numero.")
        exit(1)

    res = resistance(speed)
    watt = power_watt(res, speed)
    hp = power_hp(res, speed)

    print(f"La potenza dell'auto è uguale a {watt}W (o {hp}cv)")

if __name__ == "__main__":
    main()