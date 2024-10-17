def format_num(num: str):
    return f"({num[:3]}) {num[3:6]}-{num[6:]}"

def main():
    phone_num = input("Inserisci un numero di telefono a 10 cifre: ")
    
    if len(phone_num) != 10:
        print("Il numero inserito è più corto/lungo di 10 cifre.")
        return
    
    print(format_num(phone_num))

if __name__ == "__main__":
    main()