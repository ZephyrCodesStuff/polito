CONDITIONS = [
    "x > 0 and x < 100",
    "x > 0 or x < 100",
    "x > 0 or 100 < x",
    "x > 0 and x < 100 or x == 1",
]

def main():
    while True:
        print()

        x: str = input("Inserisci un numero: ")
        try:
            x: float = float(x)
        except ValueError:
            print("Il valore inserito non è un numero!")
            main()

        for condition in CONDITIONS:
            result = eval(f"{condition}")
            print(f'La condizione "{condition}" è {"VERA" if result else "FALSA"}')


if __name__ == "__main__":
    main()