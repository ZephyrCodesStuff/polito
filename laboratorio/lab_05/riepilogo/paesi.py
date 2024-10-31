from enum import Enum

PLURAL_COUNTRIES = [
    "etats-unis",
    "pays-bas"
]

MALE_COUNTRIES = [
    "belize",
    "cambodge",
    "mexique"
]

VOWELS = ['a', 'e', 'i', 'o', 'u']

def infer(str: str) -> int:
    str_strip = str.lower().strip() # Ignora errori di formattazione

    if str_strip in PLURAL_COUNTRIES:
        return 2
    elif str_strip in MALE_COUNTRIES:
        return 0
    elif str_strip.endswith("e"):
        return 1
    else:
        return 0

def format(gender: int, str: str) -> str:
    elided = False

    for vowel in VOWELS:
        if str.lower().strip().startswith(vowel):
            elided = True
            break

    if gender == 0:
        return f"Le {str}" if not elided else f"L'{str}"
    if gender == 1:
        return f"La {str}" if not elided else f"L'{str}"
    if gender == 2:
        return f"Les {str}"

def main():
    country = input("Inserisci il nome di un paese (in Francese): ")
    gender = infer(country)

    print(format(gender, country))

if __name__ == "__main__":
    main()