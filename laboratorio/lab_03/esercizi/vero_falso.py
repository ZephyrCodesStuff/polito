from math import sqrt

def main():
    pairs = [
        (1, 1),
        (1, 1.0),
        (2.0, sqrt(4)),
        ('1', 1),
        ('ciao', 'Ciao')
    ]

    for (var_1, var_2) in pairs:
        if var_1 == var_2:
            print(f"[+] {var_1} is equal to {var_2}")
        else:
            print(f"[!] {var_1} is NOT equal to {var_2}")

if __name__ == "__main__":
    main()