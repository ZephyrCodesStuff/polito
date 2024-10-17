import re

REGEX_EXPR = "^[A-Z][a-zA-Z0-9]+\.$"

def main():
    while True:
        message = input("Inserisci un messaggio: ")
        matches = re.match(REGEX_EXPR, message)

        if matches is not None:
            print("[+] Il messaggio è conforme al formato prestabilito!")
        else:
            print("[!] Il messaggio NON è conforme al formato prestabilito!")

if __name__ == "__main__":
    main()