from math import pi, pow

DIELECTRIC_CONST = 8.8541878188 * float(pow(10, -12))

def electric_force(charge_1: float, charge_2: float, distance: float):
    return (charge_1 * charge_2) / (4 * pi * DIELECTRIC_CONST * pow(distance, 2))

def main():
    charge_1 = float(input("Inserire la prima carica (Q1): "))
    charge_2 = float(input("Inserire la seconda carica (Q2): "))

    distance = float(input("Inserire la distanza (r): "))

    force = electric_force(charge_1, charge_2, distance)
    print(f"La forza elettrica è uguale a: {force} N")
    
if __name__ == "__main__":
    main()