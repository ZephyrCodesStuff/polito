from math import pow, pi

def diameter(wire_gauge):
    return 0.127 * pow(92, (36-wire_gauge)/39)

COPPER_RESISTANCE = 1.678 * pow(10, -8)
def copper_wire_resistance(length, wire_gauge):
    return (4 * COPPER_RESISTANCE * length) / (pi * pow(wire_gauge, 2))

ALUMINUM_RESISTANCE = 2.82 * pow(10, -8)
def aluminum_wire_resistance(length, wire_gauge):
    return (4 * ALUMINUM_RESISTANCE * length) / (pi * pow(wire_gauge, 2))

def main():
    length = input("Inserisci la lunghezza del filo (in metri): ")
    gauge = input("Inserisci il calibro del filo: ")

    try:
        length = float(length)
        gauge = int(gauge)
    except ValueError:
        print("I valori immessi non sono validi.")
        exit(1)

    copper = copper_wire_resistance(length, gauge)
    aluminum = aluminum_wire_resistance(length, gauge)

    print(f"Se il filo è di rame, la resisenza sarà uguale a {copper} Ω.")
    print(f"Se il filo è di alluminio, la resisenza sarà uguale a {aluminum} Ω.")

if __name__ == "__main__":
    main()