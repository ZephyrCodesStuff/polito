import re

SHORT_LEN = 3
LONG_LEN = 20

DNA_CHARS = "ACTG"

DNA_REGEX_SHORT = f"^[{DNA_CHARS}]{{3}}$"
DNA_REGEX_LONG = f"^[{DNA_CHARS}]{{20}}$"

def main():
    short_str = input("Inserisci la sequenza BREVE: ")
    if re.match(DNA_REGEX_SHORT, short_str) is None:
        print(f"La sequenza BREVE deve contenere esattamente {SHORT_LEN} caratteri '{DNA_CHARS}'!")
        exit(1)
    
    long_str = input("Inserisci la sequenza LUNGA: ")
    if re.match(DNA_REGEX_LONG, long_str) is None:
        print(f"La sequenza LUNGA deve contenere esattamente {LONG_LEN} caratteri '{DNA_CHARS}'!")
        exit(1)
        
    matches = re.findall(short_str, long_str)

    if matches is not None:
        print(f"La sequenza breve è contenuta in quella lunga {len(matches)} volte:")
        
        found_str = re.sub(short_str, f' [{short_str}] ', long_str).strip()
        print(f"> {found_str}")
    
if __name__ == "__main__":
    main()