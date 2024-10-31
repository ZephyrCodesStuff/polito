import re

REPLACE_CHAR = '_'
VOWEL_REGEX = re.compile("[aeiou]")

def main():
    text = input("Inserisci una stringa da analizzare: ")

    upper = [t for t in text if t.isupper()]
    even = [t for (i, t) in enumerate(text) if i % 2 == 0]
    replaced = VOWEL_REGEX.sub(REPLACE_CHAR, text)
    numbers = len([n for n in text if n.isnumeric()])
    vowels = [i for (i, t) in enumerate(text) if VOWEL_REGEX.match(t) is not None]

    print(f"Lettere maiuscole: {upper}")
    print(f"Lettere in posizioni pari: {even}")
    print(f"Stringa modificata: {replaced}")
    print(f"Cifre nella stringa: {numbers}")
    print(f"Indici delle vocali: {vowels}")

if __name__ == "__main__":
    main()