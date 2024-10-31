from typing import Iterable


def print_stats(numbers: Iterable):
    if len(numbers) == 0:
        print("[!] Non sono stati immessi abbastanza numeri (minimo: 1).")
        exit(0)

    print(f"Somma: {sum(numbers)}")
    print(f"Minimo: {min(numbers)} / massimo: {max(numbers)}")

    # Se il resto di una divisione per 2 è zero, il numero è divisibile quindi pari.
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n not in even] # I rimanenti sono dispari.

    print(f"Numeri pari: ({len(even)}) {even}")
    print(f"Numeri dispari: ({len(odd)}) {odd}")

def main():
    numbers = []

    while True:
        print()

        try:
            number = input("Inserisci un numero: ")
        except KeyboardInterrupt:
            print()
            print("[!] CTRL+C rilevato: termino...")
            exit(0)

        try:
            number = int(number)
            numbers.append(number)
        except ValueError:
            print("[!] Il valore inserito non è un numero.")

            print_stats(numbers)
            exit(0)

        print_stats(numbers)

if __name__ == "__main__":
    main()