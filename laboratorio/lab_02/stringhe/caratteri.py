def str_trim(string: str):
    return f"{string[:3]}...{string[-3:]}"

def main():
    string = input("Inserisci una stringa: ")
    
    if len(string) <= 6:
        print(string)
    else:
        print(str_trim(string))
    
if __name__ == "__main__":
    main()