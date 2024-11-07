from math import pow

def composite_interest(capital, rate, years):
    return capital * pow(1 + rate, years)

def main():
    capital = input("Inserisci il capitale iniziale: ")
    rate = input("Inserisci il tasso di interesse (da 0 a 1): ")
    years = input("Inserisci il numero di anni: ")

    try:
        capital = float(capital)
        rate = float(rate)
        years = int(years)
    except ValueError:
        print("Errore: i valori inseriti non sono numeri.")
        exit(1)
    
    print(f"Capitale dopo {years} anni: {composite_interest(capital, rate, years)}")

if __name__ == "__main__":
    main()