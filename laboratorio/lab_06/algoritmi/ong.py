def compensation(ral: float, children: int) -> int:
    if 30000 <= ral <= 40000 and children >= 3:
        return 1000 * children
    elif 20000 <= ral <= 30000 and children >= 2:
        return 1500 * children
    elif ral < 20000 and children >= 1:
        return 2000 * children
    else:
        return 0

def main():
    print("Premi CTRL+C per uscire.")

    while True:
        try:
            ral = float(input("\nInserisci il reddito annuo lordo: "))
            children = int(input("Inserisci il numero di figli: "))
        except ValueError:
            print("Errore: i valori inseriti non sono numeri.")
            continue
        except KeyboardInterrupt:
            print("\nArrivederci!")
            break
        
        if ral < 0 or children < 0:
            print("Errore: i valori inseriti non possono essere negativi.")
            continue
            
        comp = compensation(ral, children)
        if comp == 0:
            print("Non hai diritto a compensazioni.")
            continue

        print(f"La compensazione è di {comp} euro.")

if __name__ == "__main__":
    main()