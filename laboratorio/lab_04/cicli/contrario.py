import re

WORD_REGEX = re.compile('\w+')

def analyze_word(word: str):
    print()
    print(f"Analizzando: `{word}`")
    reversed = word[::-1] # Invertiamo una volta sola per motivi di prestazioni

    print(reversed) # Al contrario
    print(''.join([x for x in reversed if x.isupper()])) # Al contrario, solo maiuscole

def main():
    text = input("Inserisci una o più parole: ")
    
    # Controlla le parole nel testo
    words = WORD_REGEX.findall(text)
    
    for word in words:
        analyze_word(word)

if __name__ == "__main__":
    main()