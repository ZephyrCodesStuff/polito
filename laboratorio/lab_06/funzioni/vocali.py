VOWELS = "aeiou"

def count_vowels(s: str):

    vocali = 0
    for c in s:
        if c in VOWELS:
            vocali += 1

    return sum(1 for c in s if c in VOWELS)

def main():
    s = input("Inserisci una stringa: ")
    print(f"La stringa contiene {count_vowels(s)} vocali.")

if __name__ == "__main__":
    main()