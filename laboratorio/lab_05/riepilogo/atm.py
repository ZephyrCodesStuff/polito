PIN: int = 1234
MAX_FAILED_ATTEMPTS: int = 3

def main():
    attempts = 0

    while attempts < MAX_FAILED_ATTEMPTS:
        pin = input("Inserisci il PIN: ")

        try:
            pin = int(pin)
        except ValueError:
            print("Your PIN is invalid")
            print()
            continue # Non aumenta il counter dei tentativi
        
        if pin != PIN:
            print("Your PIN is incorrect")
            print()
            attempts += 1
            continue

        print("Your PIN is correct")
        exit(0) # 0 is the "success" error code
    
    print("Your card is blocked")
    exit(1) # 1 indicates a generic error happened

if __name__ == "__main__":
    main()