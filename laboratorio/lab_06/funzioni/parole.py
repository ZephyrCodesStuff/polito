import re

SPACE_REGEX = re.compile(r" +")

def count_words(s: str):
    s = re.sub(SPACE_REGEX, ' ', s)
    return len(s.split())

def main():
    s = input("Inserisci una stringa: ")
    print(f"La stringa contiene {count_words(s)} parole.")

if __name__ == "__main__":
    main()