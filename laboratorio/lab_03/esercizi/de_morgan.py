CONDITIONS = [
    ("not(x > 0 and x < 100)",              "not x > 0 or not x < 100",),
    ("not(x > 0 or x < 100)",               "not x > 0 and not x < 100",),
    ("not(x > 0 or 100 < x)",               "not x > 0 and not 100 < x"),
    ("not(x > 0 and x < 100 or x == 1)",    "not x > 0 or not x < 100 and not x == 1"),
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

        for (condition, condition_alt) in CONDITIONS:
            result = eval(condition)
            result_alt = eval(condition_alt)

            # Le due condizioni devono essere uguali -- altrimenti De Morgan è stato applicato male
            try:
                assert result == result_alt
            except AssertionError:
                print("La legge di De Morgan è stata applicata male: le due condizioni non combaciano!")
            
            print(f'La condizione "{condition}" è {"VERA" if result else "FALSA"}')
            print(f'La condizione (con De Morgan applicato) "{condition_alt}" è {"VERA" if result_alt else "FALSA"}')
            print()


if __name__ == "__main__":
    main()